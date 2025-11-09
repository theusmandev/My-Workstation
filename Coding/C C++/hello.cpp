// #include <iostream>
// using namespace std;

// int main() {
//     cout << "Hello, World!" << endl;
//     return 0;
// }




#include <iostream>
#include <cstring>
using namespace std;

class Student {
    char *name;

public:
    Student(const char *n) {
        name = new char[strlen(n) + 1];
        strcpy(name, n);
    }

    // Default shallow copy constructor (compiler generated)
    void display() {
        cout << "Name: " << name << endl;
    }

    ~Student() {
        delete[] name;
        cout << "Destructor called!" << endl;
    }
};

int main() {
    Student s1("Usman");
    Student s2 = s1; // 👈 Shallow copy (default copy constructor)

    s1.display();
    s2.display();
}
