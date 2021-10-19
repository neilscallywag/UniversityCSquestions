#include <iostream>
void increment(float& const value) {
	value++;
}
// LEARNING Inheretence -> 3

class Entity {
public: 
	float x, y, speed;
	void Move(float& xa, float& ya) {
		x += xa * speed;
		y += ya * speed;
	}
};

class Player: public Entity { 
//new data type eg int var it will be Player var has inherited position properties from entity class
public:
	Player(float X, float Y, float S) { // initilisation 
		x = X;
		y = Y;
		speed = S;

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
	/// LEARNING CLASSES -> 1;

	Player player(5.0, 5.0, 1.0);

	Player player2(2.0, 2.0, 1.0);
		for (static int i; i < 10; i++) {
			increment(player.x);
			increment(player2.x);
		}

	player.Move(player.x, player.y);
	player2.Move(player2.x, player2.y);

	std::cout << player.x << " " << player.y << std::endl;
	std::cout << player2.x << " " << player2.y << std::endl;


	/// LEARNING ENUMS -> 2
	Log log;
	log.SetLevel(Log::Level::LError);
	log.Warn("a!"); // doesnt get called 
	log.ErrorM("q!");

}