#include <cassert>
#include <iostream>
#include "array_list.cpp"

void test_empty_array_has_length_zero(){
    ArrayList list{}; 
    std::cout << "Does an empty array have a length of 0?\n";
    assert(list.length() == 0);
    std::cout << "Yup\n";
}

void test_array_with_two_elements_appended_has_length_two(){
    ArrayList list{}; 
    list.append(10); 
    list.append(15); 
    std::cout << "Does an empty array with two appended elements have a length of 2?\n";
    assert(list.length() == 2); 
    std::cout << "Yeah\n"; 
}

void test_print(){
    ArrayList list{}; 
    list.append(3); 
    list.append(5); 
    list.print();
}

void test_operator_overload_read_write(){
    ArrayList list{}; 
    list.append(4);
    list.append(7);
    assert(list[0] == 4 );
    std::cout << "woop\n";
    
    list[1] = list[0];
    assert(list[1] == list[0]);
    std::cout << "yay\n";
}

void test_vector_constructor(){
    ArrayList primes({2, 3, 5, 7, 11});
    primes.print();
    std::cout<<"\n";

}

void test_remove(){
    ArrayList example({0,2,4,6,8,10});
    example.remove(2);
    example.print();
    std::cout<<"\n";
}


void test_pop_at_index(){
    ArrayList example({0,2,4,6,8,10});
    assert(example.pop(2)==4);
}

void test_pop(){
    ArrayList example({0,2,4,6,8,10});
    assert(example.pop()==10);
}

void test_insert()
{
    ArrayList a{{0, 1}};
    assert(a.length() == 2);
    a.insert(42, 0);
    assert(a.length() == 3);
    assert(a[0] == 42);
    assert(a[1] == 0);
    assert(a[2] == 1);
    a.insert(43, 1);
    assert(a.length() == 4);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    a.insert(44, 4);
    assert(a.length() == 5);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    assert(a[4] == 44);
    std::cout << "test_size completed successfully\n";
}

void test_shrink_to_fit(){
    ArrayList list{};
    for(int i=0; i<63; i++){
        list.append(0);
    }
    assert(list.capacity()==64);
    for(int i=0; i<51;i++){
        list.remove(0);
    }
    assert(list.capacity()==16);
}

int main(){
    test_empty_array_has_length_zero(); 
    test_array_with_two_elements_appended_has_length_two(); 
    test_print();
    test_insert(); 
    test_operator_overload_read_write();
    test_vector_constructor();
    test_remove();
    test_pop_at_index();
    test_pop();
    test_shrink_to_fit();
    return 0; 
}