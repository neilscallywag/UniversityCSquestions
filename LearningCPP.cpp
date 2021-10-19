#include <iostream>
void increment(int& const value) {
	value++;
}

class Player { //new data type eg int var it will be Player var
public:
	int x, y, speed;
	Player(int X, int Y, int S) {
		x = X;
		y = Y;
		speed = S;

	}
	void Move(int& xa, int& ya) {
		x += xa * speed;
		y += ya * speed;
	}
};

class Log {
public:
	enum class Level : unsigned char {
		LError = 0, LWarning, LInfo
	};
private:
	Level m_LogLevel = Level::LInfo;
public:
	void SetLevel(Level level) {
		m_LogLevel = level;
	}
	void ErrorM(const char* message)
	{
		if (m_LogLevel >= Level::LError)
			std::cout << "[Error]" << message << std::endl;
	}
	void Warn(const char* message)
	{
		if (m_LogLevel >= Level::LWarning)
			std::cout << "[Warning]" << message << std::endl;
	}
	void Info(const char* message)
	{
		if (m_LogLevel >= Level::LInfo)
			std::cout << "[Info]" << message << std::endl;
	};
};
int main() {
	/// LEARNING CLASSES;

	Player player(5, 5, 1);

	Player player2(2, 2, 1);
		for (static int i; i < 10; i++) {
			increment(player.x);
			increment(player2.x);
		}

	player.Move(player.x, player.y);
	player2.Move(player2.x, player2.y);

	std::cout << player.x << " " << player.y << std::endl;
	std::cout << player2.x << " " << player2.y << std::endl;


	/// LEARNING ENUMS
	Log log;
	log.SetLevel(Log::Level::LError);
	log.Warn("a!");
	log.ErrorM("q!");

}