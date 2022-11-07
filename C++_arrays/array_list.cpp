#include <iostream>
#include <stdexcept>
#include <cmath>
#include <vector>

class ArrayList{
    private: 
    
    int *_data; 
    int _capacity = 1; 
    int _size = 0;
    int _growth = 2; //growth factor
    
    /*
    ekstender capacity, slik at _size er mindre eller lik kapasiteten
    */
    void resize(){
        _capacity *= _growth; 
        int *new_data = new int[_capacity];
        for (int i = 0; i < _size; i++){
            new_data[i] = _data[i];
        } 
        delete[] _data; 
        _data = new_data;
    }
    /**
    Minsker størrelsen på arrayet til nærmeste 2^n
    */
    void shrink_to_fit(){
        int n = 1;
        int new_cap = _growth;
        while (new_cap < _size){
            new_cap = std::pow(2, n); 
            n++;  
        }
        _capacity = new_cap; 
    }
    public: 
    /*
    contructor som henter data
    */
    ArrayList(){
        /*
        Lagen en array med integere som er like stor som capacityen
        */
        _data = new int[_capacity]; 
    }
        /*
        overskriver arraylist-metoden slik at den kan ta inn vektorer også
        */
    ArrayList(std::vector<int> data)
    {
        _data = new int[_capacity];
        for (int i = 0; i < _capacity; i++)
        {
            _data[i] = 0;
        }
        for (int x : data)
        {
            append(x);
        }
    }

    ~ArrayList(){
        //destructor 
        delete[] _data; 
    }

    /*
    returnerer lengden
    */
    int length(){
        return _size; 

    }

    /*
    returnerer kapasiteten
    */
    int capacity(){
        return _capacity;
    }

    /*
    som en get-funksjon, returnerer verdien til en bestemt verdi i listen
    */
    int& operator[](int index){
        if (index > _size){
            throw std::range_error("List indxex out of range");
        } 
        return _data[index];
    }

    /*
    sletter et valgt element
    */
    void remove(int x){
        for(int i = 1; i<_size-x+1; i++){
            _data[x+i-1]=_data[x+i];
        }
        _size--;
        if(_size<0.25*_capacity){
            shrink_to_fit();
        }
    }
    /*
    sletter et valgt element og returnerer elementet
    */
    int pop(int x){
        int inital=_data[x];
        for(int i = 1; i<_size-x+1; i++){
            _data[x+i-1]=_data[x+i];
        }
        _size--;
        if(_size<0.25*_capacity){
            shrink_to_fit();
        }
        return inital;
    }

    /*
    Sletter og retrnerer siste element
    */
    int pop(){
        int pop= _data[_size-1];
        _size--;
        return pop;

    }

    /*
    Legg til et element på slutten av listen
    */
    void append(int x){
        if (_size >= _capacity) {
            resize();
        }
        _data[_size] = x; 
        _size++;
    }

    /*
    printer ut hele listen
    */
    void print()
    {
        for (int i = 0; i < _size; i++){
            std::cout << _data[i] << ", "; 
        }
    }
    
    /*
    legger til et valgt element på en bestemt plass i listen
    */
    void insert(int val, int index){
        if (index > _size){
            throw std::range_error("Index out of range"); 
        }
        append(val);
        if (index < _size){    
            int tmp = 0; //Temporary storage variable
            for (int i = _size-1; i > index; i--){ 
                tmp = _data[i-1];
                _data[i-1] = _data[i];
                _data[i] = tmp; 
            }
        }
    }
};