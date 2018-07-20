#include <iostream>
#include <fstream>

int main()
{

    std::ofstream myfile;
    myfile.open("example.txt");
    myfile << "First Name=Eva\n";
    myfile << "Last Name=Dotterer";
    myfile.close();
    return 0;
}
