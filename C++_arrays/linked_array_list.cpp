#include <iostream>
#include <memory> 
#include <stdexcept>
#include <vector> 

#include "array_list.cpp"
#include "linked_list.cpp"

struct ArrayListNode{
    std::unique_ptr<ArrayList> value;

    ArrayListNode *next = nullptr; 
    ArrayListNode *prev = nullptr;

    ArrayListNode(std::vector<int> vec_val, ArrayListNode *prev, ArrayListNode *next){
  
        value = std::make_unique<ArrayList>(vec_val);
        this->next = next;
        this->prev = prev;   

    }
};

class LinkedArrayList{
    private: 
    ArrayListNode *head = nullptr;
    ArrayListNode *tail = nullptr;
    int _size = 0; 

    public:
    LinkedArrayList(){
        
    }
};

int main()
{
    ArrayListNode node({1, 2, 3}, nullptr, nullptr);
    node.value->print();
}