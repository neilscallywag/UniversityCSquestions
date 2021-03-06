#include <iostream>
#include <string>
void increment(float& const value) {
	value++;
}
// LEARNING Inheretence -> 3
template <typename T>
void Print(T var) {
std::cout << var << std::endl;
}
class Entity {
public: 
	float x;
	float y;
	float speed =1  ; // need deref pointer as cannot multiply/divide pointer by float


	Entity() {};

	void Move(float &xa, float &ya) {
		x += xa * (speed);
		y += ya * (speed); // need to dereference because memory address and contents r different

		
	}

	 virtual void GetDetails() {
		std::cout << x << " " << y << " " << speed << std::endl;
	}
};




class Player : public Entity {
//new data type eg int var it will be Player var has inherited position properties from entity class
public:
	const char* name;
	Player(float X, float Y, float S, const char* Name) { // initilisation 
		x = X;
	    y = Y;
		speed = S;
		name = Name;
		
	}
	void GetDetails() {
		std::cout << x << " " << y << " " << speed << std::endl;
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

	Player player(5.0, 5.0, 1.0, "Neil");
	Player player2(2.0, 2.0, 1.0, "test");
	Entity entity;
	entity.x = 3.0;
	entity.y = 3.0;

std::cout << "ENV " << std::endl;
	player.GetDetails();
	player2.GetDetails();
	entity.GetDetails();
std::cout << "ENV " << std::endl;



	
	
	for (static int i; i < 10; i++) {
			increment(player.x);
			increment(player2.x);
		}

	player.Move(player.x, player.y); // Method Move inhereted from Entity Class
	player2.Move(player2.x, player2.y); 

	std::cout << player.x << " " << player.y << " " << player.name << " " << player.speed << " " << std::endl;
	std::cout << player2.x << " " << player2.y << " " << player2.name << " " << player2.speed << " " << std::endl;
	std::cout << "Size of Player Class: " << sizeof(Player) << std::endl << "Size of Entity Class  " << sizeof(Entity) << std::endl;
	// Size of Player = Size of Entity(12 bytes) + Const Char Name (4bytes)
	// Size of Char is 4 bytes instead of 1 because Name is int type (N->ASCII)

	Print<std::string>("abc");
	/// LEARNING ENUMS -> 2
	Log log;
	log.SetLevel(Log::Level::LError);
	log.Warn("a!"); // doesnt get called 
	log.ErrorM("q!");

}