#include<iostream>
#include<string.h>
#include<bitset>
using namespace std;

string substitute(string s,int *st)
{
	string sub="";
	for(int i=0;i<4;i++)
	{
		bitset<4> bin(s.substr(4*i,4));
		int ibin  = bin.to_ulong();
		bitset<4> bit(st[ibin]);
		string st = bit.to_string();
		sub=sub+st;
	}
	return sub;
}
string permutation(string s,int *pt)
{
	string per="";
	for(int i=0;i<16;i++)
	{
		per = per+s[pt[i]];
	}
	return per;
}
class Encrypt
{
	private:
		string key;
		int st[16] = {14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7};
		int pt[16] = {0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15};
	public:
		Encrypt()
		{
			key = "00111010100101001101011000111111";	
		}
		string encrypt(string plaintext)
		{
			string ct;
			int n = 5;
			string u[4];
			string v[4];
			string w[4];
			string subkeys[n];
			if(plaintext.length() != 16) 
			{
            	cout << "Input plaintext must be exactly 16 bits." << endl;
            	return ct;
        	}
			for(int i=0;i<n;i++)
			{
				subkeys[i]=key.substr(4*i,16);
			}
			w[0]=plaintext;
			for(int i=0;i<4;i++)
			{
				if(i<3)
				{
					bitset<16> binsubkey(subkeys[i]);
					bitset<16> binplaintext(w[i]);
					bitset<16> binu(binsubkey^binplaintext);
					u[i] = binu.to_string();
					v[i]=substitute(u[i],st);
					w[i+1]=permutation(v[i],pt);
				}
				else
				{
					bitset<16> binsubkey(subkeys[i]);
					bitset<16> binplaintext(w[i]);
					bitset<16> binu(binsubkey^binplaintext);
					u[i] = binu.to_string();
					v[i]=substitute(u[i],st);
					bitset<16> fin(v[i]);
					bitset<16> skey(subkeys[i+1]);
					bitset<16> fina(fin^skey);
					ct= fina.to_string();
				}
		    }
		    for(int i=0;i<4;i++)
			{
				cout<<"W["<<i<<"]:"<<w[i]<<endl;
				cout<<"K["<<i<<"]:"<<subkeys[i]<<endl;
				cout<<"U["<<i<<"]:"<<u[i]<<endl;
				cout<<"V["<<i<<"]:"<<v[i]<<endl;
			}
		    return ct;
		}
		
};
class Decrypt
{
	private:
		string key;
		int rst[16]={14,3,4,8,1,12,10,15,7,13,9,6,11,2,0,5};
		int rpt[16]={0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15};
	public:
		Decrypt()
		{
			key = "00111010100101001101011000111111";
		}
		string decrypt(string ciphertext)
		{
			string pt;
			int n = 5;
			string u[4];
			string v[4];
			string w[4];
			string subkeys[n];
			for(int i=0;i<n;i++)
			{
				subkeys[i]=key.substr(4*i,16);
			}
			w[3]=ciphertext;
			for(int i=3;i>=0;i--)
			{
				if(i==3)
				{
					bitset<16> ct(ciphertext);
					bitset<16> binsubkey(subkeys[i+1]);
					bitset<16> result(ct^binsubkey);
					string s = result.to_string();
					v[i]=s;
					u[i]=substitute(v[i],rst);
					bitset<16> binsubkey2(subkeys[i]);
					bitset<16> binu(u[i]);
					bitset<16> result1(binsubkey2^binu);
					string s1 = result1.to_string();
					w[i]=s1;
					
				}
				else
				{
					string s2 = permutation(w[i+1],rpt);
					v[i]=s2;
					u[i]=substitute(v[i],rst);
					bitset<16> binui(u[i]);
					bitset<16> binsk(subkeys[i]);
					bitset<16> res(binui^binsk);
					string s3 = res.to_string();
					w[i]=s3;
				}
		    }
		    for(int i=3;i>=0;i--)
			{
				cout<<"W["<<i<<"]:"<<w[i]<<endl;
				cout<<"K["<<i<<"]:"<<subkeys[i]<<endl;
				cout<<"U["<<i<<"]:"<<u[i]<<endl;
				cout<<"V["<<i<<"]:"<<v[i]<<endl;
			}
			pt=w[0];
		    return pt;
		}
};
int main()
{
	Encrypt enc;
	Decrypt dec;
	string plaintext;
	string ciphertext;
	int choice;
	cout<<"1.Encryptoin\n2.Decryption\nEnter choice:";
	cin>>choice;
	switch(choice)
	{
		case 1:
			cout<<"Enter Plain Text:";
			cin>>plaintext;
			ciphertext=enc.encrypt(plaintext);
			cout<<"Cipher Text:"<<ciphertext;
			break;
		case 2:
			cout<<"Enter Cipher Text:";
			cin>>ciphertext;
			plaintext=dec.decrypt(ciphertext);
			cout<<"Plain Text:"<<plaintext;
			break;
		default:
			cout<<"Invalid Choice";
	}
	cout<<endl;
}
