#include <iostream>
#include <vector>

struct Node {
    int value;
    Node *next = nullptr;
    Node *previous = nullptr;
};

class LinkedList
{
  private:
    Node *head = nullptr;
    Node *tail= nullptr;
    int _size = 0;

  public:
    //constructor
    LinkedList(){
    }

    /**
     * Create a linked list with a vector
     * @param vector The vector from which the linked list will be based on 
     **/
    LinkedList(std::vector<int> vector_list){
        for (int e: vector_list){
            append(e);
        }
    }

    //destructor
    ~LinkedList()
    {
        Node *current = head;
        Node *next = head;
        while (current != nullptr) {
            next = current->next;
            delete current;
            current = next;
        }
    }

    //Returns size of the linked list
    int length()
    {
        return _size;
    }

    /**
    * Append a value at the end of a linked list
    * @param value Value to be appended 
    **/
    void append(int value)
    {
        Node *node = new Node{value};
        _size++;
        if (head == nullptr)
        {
            head = node;
            return;
        }
        Node *current = head;
        while (current->next != nullptr)
        {
            current = current->next;
        }
        current->next = node;
    }

    //Prints a linked list 
    void print()
    {
        std::cout << "[ ";
        Node *current = head;
        while (current != nullptr) {
            std::cout << current->value << " ";
            current = current->next;
        }
        std::cout << "]\n";
    }

    //Overloads [] operator
    int &operator[](int index)
    {
        int current_index = 0;
        Node *current = head;
        while (current != nullptr)
        {
            if (current_index == index)
            {
                return current->value;
            }
            current = current->next;
            current_index++;
        }
        throw std::out_of_range("Index " + std::to_string(index) + " is out of range.");
    }


    /**
    * Insert a value in a linked list. 
    * @param val value to be inserted
    * @param index index of inserted value
    **/
    void insert(int val, int index){
        if ((index > _size) or (index < 0)){
            throw std::range_error("List index out of range"); 
        }
        int current_index = 0; 
        if (current_index == index){
            append(val);
            return;  
        }

        Node *current = head;
            while (current_index < index){
                current = current->next; 
                current_index++; 
            }//block ends when current_index == index
        
        int tmp = current->value;
        current->value = val; 
        int tmp2 = 0; //arbitrary value for second tmp var 
        current = current->next; 
        current_index++; 

        int fin_val = 0; //final value to append, 0 is arbitray

            while (current != nullptr){
                tmp2 = current->value; 
                current->value = tmp; 
                tmp = tmp2;
                fin_val = tmp;
                current = current->next; 
            }
    append(fin_val);
    }
  
      /**
    * Remove a value in a linked list. 
    * @param index index of value to be deleted
    **/
    void remove(int index){
      if ((index>=_size) or (index<0)){
        throw std::range_error("out of range");
      }
      int current_index=0;
      Node *current=head;
      while(current != nullptr){
        if(current_index>=index){
            current->value=current->next->value;
            if(current->next->next==NULL){
                current->next=NULL;
                _size--;
                 return;
            }
           }
        if(current_index==_size-2){
            current->next=NULL;
            _size--;
            return;
        }
        current=current->next;
        current_index++;
      }
    }

    /**
    *Removes element at index and returns said element 
    * @param index index of inserted value
    * @return element deleted at index
    **/
    int pop(int index){
        if ((index>=_size) or (index<0)){
        throw std::range_error("out of range");
      }
      int current_index=0;
      Node *current=head;
      int verdi;
      while(current != nullptr){
        if (current_index==index){
            verdi=current->value;
        }
        if(current_index>=index){
            current->value=current->next->value;
            if(current->next->next==NULL){
                current->next=NULL;
                _size--;
                 return verdi;
            }
           }
        if(current_index==_size-2){
            verdi=current->next->value;
            current->next=NULL;
            _size--;
            return verdi;
        }
        current=current->next;
        current_index++;
      }
      return 0;

    }

    /**
    *Removes last element and returns it
    * @return last element 
    **/
    int pop(){
        int current_index=0;
        Node *current=head;
        int verdi;
        while(current != nullptr){
            if(current_index==_size-2){
            verdi=current->next->value;
            current->next=NULL;
            _size--;
            return verdi;
        }
        current=current->next;
        current_index++;
        }
    return 0;
    }
};
