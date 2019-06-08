#include <iostream>
using namespace std;

class Student {
    public :

    int rollNumber;
    static int totalStudents;
};

int Student::totalStudents = 20;

int main() {
    Student s;
    // Correct statement to access totalStudents
    cout << s.totalStudents << endl;
}
