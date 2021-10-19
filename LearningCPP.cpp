#include <iostream>
void increment(int& const value) {
	value++;
}

class Player { //new data type eg int var it will be Player var
public:
	int x, y, speed;


	void Move(int& xa, int& ya) {
		x += xa * speed;
		y += ya * speed;
	}
};

class Log {
public:
	enum Level {
		LError = 0, LWarning, LInfo
	};
private:
	Level m_LogLevel = LInfo;
public:
	void SetLevel(Level level) {
		m_LogLevel = level;
	}
	void ErrorM(const char* message)
	{
		if (m_LogLevel >= LError)
			std::cout << "[Error]" << message << std::endl;
	}
	void Warn(const char* message)
	{
		if (m_LogLevel >= LWarning)
			std::cout << "[Warning]" << message << std::endl;
	}
	void Info(const char* message)
	{
		if (m_LogLevel >= LInfo)
			std::cout << "[Info]" << message << std::endl;
	};
};
int main() {
	/// LEARNING CLASSES;

	Player player;
	player.x = 5;
	player.y = 5;
	player.speed = 1;

	Player player2;
	player2.x = 2;
	player2.y = 2;
	player2.speed = 1;

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
	log.SetLevel(Log::LError);
	log.Warn("Hello!");
	log.ErrorM("World!");

}