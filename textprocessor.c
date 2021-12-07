#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct tnode
{
  struct tnode *parent;
  struct tnode *children[27];
};

int map(char ch)
{
  return ch - 'a';
}

struct tnode *add_node(struct tnode *p)
{
  struct tnode *new = malloc(sizeof(struct tnode));
  int i;
  new->parent = p;
  for(i=0;i<27;i++) new->children[i] = NULL;
  return new;
}

void trie_free(struct tnode *root)
{
  int i;
  for(i=0;i<27;i++)
    {
      if(root->children[i])
	trie_free(root->children[i]);
    }
  free(root);
}

void trie_insert(struct tnode *root,char *str,int s,int e)
{
  if(s == e)
    {
      if(!root->children[map('{')]) root->children[map('{')] = add_node(root);
      return;
    }
  if(!root->children[map(str[s])]) root->children[map(str[s])] = add_node(root);
  trie_insert(root->children[map(str[s])],str,s+1,e);
}

void print(struct tnode *root)
{
  int i;
  printf("{\n");
  for(i=0;i<26;i++)
    {
      if(root->children[i])
	{
	  printf("%c\n",'a'+i);
	  print(root->children[i]);
	}
    }
  printf("}\n");
}

int nobranch(struct tnode *root)
{
  int i,c = 0;
  for(i=0;i<27;i++)
    {
      if(root->children[i]) c++;
      if(c > 1) return 0;
    }
  return 1;
}

struct tnode *find(struct tnode *root,char *str,int s,int e)
{
  for(;s<e;s++)
    root = root->children[map(str[s])];
  return root;
}

void build(struct tnode *root,char *str,int s,int e)
{
  int i;
  for(i=e-1;i>=s;i--)
    trie_insert(root,str,i,e);
  root->children[26] = add_node(root);
}

void append(struct tnode *root,char ch)
{
  int i;
  for(i=0;i<26;i++)
    {
      if(root->children[i])
        append(root->children[i],ch);
    }
  if(root->children[26])
    {
      root->children[26] = NULL;
      if(!root->children[map(ch)])
	root->children[map(ch)] = add_node(root);
      if(!root->children[map(ch)]->children[26])
	root->children[map(ch)]->children[26] = add_node(root->children[map(ch)]);
    }
}

void edit(struct tnode *root,char *str,int s,int e)
{
  struct tnode *bottom = find(root,str,s-1,e-1);
  int i;
  for(;nobranch(bottom->parent);bottom=bottom->parent) {}
  for(i=0;i<27 && bottom->parent->children[i]!=bottom;i++) {}
  bottom->parent->children[i] = NULL;
  trie_free(bottom);
  append(root,str[e-1]);
  root->children[map('{')] = add_node(root);
}

int count(struct tnode *root)
{
  int i,c = 0;
  for(i=0;i<26;i++)
    if(root->children[i]) c += 1 + count(root->children[i]);
  return c;
}

int main()
{
  int qs,width,len,i,start,subs[100000];
  char doc[100001];
  struct tnode *trie = add_node(NULL);
  scanf("%s",doc);
  scanf("%d %d",&qs,&width);
  for(len=strlen(doc),i=0;i<=len-width;i++)
    {
      if(!i)
	build(trie,doc,0,width);
      else
	edit(trie,doc,i,i+width);
      subs[i] = count(trie);
    }
  trie_free(trie);
  for(i=0;i<qs;i++)
    {
      scanf("%d",&start);
      printf("%d\n",subs[start-1]);
    }
}
