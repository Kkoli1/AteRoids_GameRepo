#include <string>

class Logger {
public:
	static Logger& get_instance() {
		static Logger logger{};
		return logger;
	}
	
	void write(const std::string& str) noexcept {
		// write log information in the file 
	}
	
	void remove(const std::string&);
	std::string read() noexcept;
	
private:
	Logger() = default;
	~Logger() {
		// save file
	}
	Logger(const Logger&) = delete;
	Logger(Logger&&) = delete;
	
	Logger& operator=(const Logger&) = delete;
	Logger& operator=(Logger&&) = delete;
};

class Game {
	int m_score {};	
};

class GameEntityFactory {
	
};

class AsteroidFactory: public GameEntityFactory{
	
};

class SpaceshipFactory: public GameEntityFactory{
	const int const * m_damage {nullptr};
};

class StarsFactory: public GameEntityFactory{
	
};

class SpaceDebrisFactory: public GameEntityFactory{
	
};
