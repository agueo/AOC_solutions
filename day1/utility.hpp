#ifndef _UTILITY_H_
#define _UTILITY_H_

#include <vector>
#include <string>

/**
 * @briefutility func for getting data into vector
 * @param filename - filename of file to get data from
 */
std::vector<int> getDataFromFile(std::string &filename);

// implement slicing for vectors
/**
 * \brief make a slice of a vector returning just the elements you ask for
 *
 * \param v - reference to a vector of any type
 * \param m - starting index of slice
 * \param n - ending index of slice
 * \returns - vector sliced with only asked for indices
 */
template<typename T>
std::vector<T> make_slice(std::vector<T> &v, int m, int n) {
    std::vector<T> vec (n - m + 1);
    std::copy(v.begin() + m, v.begin() + n+1, vec.begin());
    return vec;
}

#endif
