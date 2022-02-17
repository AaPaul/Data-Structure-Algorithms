//#include <iostream>
//
//using namespace std;
//#include <utility>
//
//float fib(float n)
//{
//    if (n>2)
//    {
//        return fib(n-1)+fib(n-2);
//    }
//    else if (n<1)
//    {
//        cout<<"Error!"<<endl;
//        return -1;
//    }
//    else
//        return n-1;
//}
//
//int main()
//{
//    int n;
//    cin>>n;
//    cout<<fib(n)<<endl;
//    return 0;
//}

#include <utility>
#include <stdint.h>
#include <iostream>
using namespace std;
std::pair<uint64_t, uint64_t> Fib(size_t n)
{
  // ����F_{n}��F_{n + 1}, ע���Ƕ�UINT64_MAXȡģ�Ľ��.
  if (n > 0)
  {
    auto PF = Fib(n / 2);   // ���ڵݹ����.
    auto t0 = PF.first;
    auto t1 = PF.second;
    if (n % 2 == 1)         // �������.
      return {t0 * t0 + t1 * t1, (2 * t0 + t1) * t1};
    else
      return {(2 * t1 - t0) * t0, t0 * t0 + t1 * t1};
  }
  return {0, 1};            // ��������: F_0��F1.
}

