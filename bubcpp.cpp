#include <vector>

int twoCitySchedCost(std::vector<std::vector<int>> &costs)
{
    std::sort(costs.begin(),
              costs.end(),
              [](std::vector<int> v, std::vector<int> w) { return v[0] + w[1] < v[1] + w[0] })

        for (auto &val : costs)
    {
        std::cout << val[0] << "," << val[1] << std::endl;
    }

    return 0
}

int main()
{
}
