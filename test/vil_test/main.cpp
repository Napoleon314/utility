#include <vil/cpu_info.h>

using namespace vil;

int main()
{
	auto c = get_cpu_count();
	printf("cpu: %d\n", c);
	return 0;
}
