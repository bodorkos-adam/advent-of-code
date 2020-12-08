#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

namespace {

std::vector<int> readInput()
{
    std::vector<int> numbers;
    std::ifstream file("input.txt");
    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        int number;

        iss >> number;
        numbers.push_back(number);
    }

    std::sort(numbers.begin(), numbers.end());

    return numbers;
}

int p1(std::vector<int> const& numbers)
{
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            auto num1 = numbers[i];
            auto num2 = numbers[j];
            auto sum2 = num1 + num2;

            if (sum2 > 2020)
                break;

            if (sum2 == 2020)
                return num1 * num2;
        }
    }

    return 0;
}

int p2(std::vector<int> const& numbers)
{
    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            auto num1 = numbers[i];
            auto num2 = numbers[j];
            auto sum2 = num1 + num2;

            if (sum2 > 2020)
                break;

            for (int k = j + 1; k < numbers.size(); ++k) {
                auto num3 = numbers[k];
                auto sum3 = sum2 + num3;

                if (sum3 > 2020)
                    break;

                if (sum3 == 2020)
                    return num1 * num2 * num3;
            }
        }
    }

    return 0;
}

} // namespace

int main()
{
    auto numbers = readInput();

    std::cout << p1(numbers) << std::endl;
    std::cout << p2(numbers) << std::endl;

    return 0;
}
