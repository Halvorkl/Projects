#include <chrono>    // for high_resolution_clock
#include <fstream>   // for ofstream
#include <iostream>  // for cout
#include <stdexcept> // for runtime_error

#include "array_list.cpp"
#include "linked_list.cpp"

using namespace std::chrono;

void run_array_list_get()
{
    std::cout << "\nArray list - get \n";
    std::ofstream ofs{"array_list_get.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    // Number of times we want to
    int runs = 1000;
    for (int N = 100; N < 1E6; N *= 10)
    {

        ArrayList ll{};
        for (int i = 0; i < N; i++)
        {
            ll.append(i);
        }
        auto start = high_resolution_clock::now();
        // Get value in the middle
        for (int run = 0; run < runs; run++)
        {
            auto value = ll[N / 2];
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)runs << "\n";
        ofs << N << " " << duration.count() / (double)runs << "\n";
    }
}

void run_array_list_insert_front()
{
    std::cout << "Array list - insert front \n";
    std::ofstream ofs{"array_list_insert.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    for (int N = 100; N < 1E6; N *= 10)
    {
        auto start = high_resolution_clock::now();
        ArrayList a{};
        for (int i = 0; i < N; i++)
        {
            a.insert(i, 0);
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)N << "\n";
        ofs << N << " " << duration.count() / (double)N << "\n";
    }
}

void run_linked_list_get()
{
    std::cout << "\nLinked list - get \n";
    std::ofstream ofs{"linked_list_get.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    // Number of times we want to
    int runs = 1000;
    for (int N = 100; N < 1E6; N *= 10)
    {

        LinkedList ll{};
        for (int i = 0; i < N; i++)
        {
            ll.append(i);
        }
        auto start = high_resolution_clock::now();
        // Get value in the middle
        for (int run = 0; run < runs; run++)
        {
            auto value = ll[N / 2];
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)runs << "\n";
        ofs << N << " " << duration.count() / (double)runs << "\n";
    }
}

void run_linked_list_insert_front()
{
    std::cout << "Linked list - insert front \n";
    std::ofstream ofs{"linked_list_insert.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    for (int N = 100; N < 1E6; N *= 10)
    {
        auto start = high_resolution_clock::now();
        LinkedList a{};
        for (int i = 0; i < N; i++)
        {
            a.insert(i, 0);
        }

        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << N << " " << duration.count() / (double)N << "\n";
        ofs << N << " " << duration.count() / (double)N << "\n";
    }
}

int main(){
    run_array_list_get();
    run_array_list_insert_front();
    run_linked_list_get();
    run_linked_list_insert_front();
}