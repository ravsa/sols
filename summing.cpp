#include <iostream>
int main()
{
    int arr[6] = {1, 3, 7, 9, 10, 11};
    int size = 6;
    int number = 12;
    int count = 0;
    for (int i = 0; i < size; ++i) {
        for(int j = size-1; j >= i; --j)
        {
            int sum = arr[i] + arr[j];
            if (sum == number)
                count++;
            else if (sum < number)
                break;
        }
    }
    std::cout << count << std::endl;
    return 0;
}
