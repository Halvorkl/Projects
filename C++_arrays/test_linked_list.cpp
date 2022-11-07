#include <iostream>
#include "linked_list.cpp"
#include <cassert>


void test_empty_list_has_length_zero(){
    LinkedList list;
    assert(list.length()==0);
}

void test_append(){
    LinkedList list;
    list.append(0);
    list.append(2);
    assert(list.length()==2);
}

void test_print(){
    LinkedList list;
    list.print();
    list.append(1);
    list.print();
}

void test_index_operator(){
    LinkedList list;
    list.append(1);
    list.append(2);
    assert(list[1]==2);
    assert(list[0]==1);
}

void test_insert(){
    LinkedList list; 
    list.append(19); 
    list.append(21);
    list.append(39);

    list.insert(99, 1);     
    assert(list.length() == 4);  
    assert(list[1 == 99]); 
    assert(list[0 ==19]);
    assert(list[3] == 39); 
}
  
void test_remove(){
    LinkedList list;
    list.append(0);
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);
    list.append(6);
    list.print();
    list.remove(6);
    list.print();
}

void test_pop_at_index(){
     LinkedList list;
    list.append(0);
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);
    list.append(6);
    assert(list.pop(4)==4);
}


void test_pop(){
    LinkedList list;
    list.append(0);
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);
    list.append(6);
    assert(list.pop()==6);
}

void test_vector_input(){
  LinkedList list; 
  list.append(1);
  list.append(2);

  LinkedList vec_list({1,2}); 
  for (int i; i<2; i++){
      assert(list[i] == vec_list[i]);
  }
}
  
int main()
{
    test_empty_list_has_length_zero();
    test_append();
    test_print();
    test_index_operator();
    test_insert();
    test_remove();
    test_pop();
    test_pop_at_index();
    test_vector_input(); 
    return 0;
}
