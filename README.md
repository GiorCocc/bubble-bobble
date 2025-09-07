# 🐉 Bubble Bobble - Python Game 🫧

A faithful Python recreation of the classic arcade game **Bubble Bobble** featuring dragons, bubbles, and cooperative gameplay! 🎮

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-GPL-green.svg)
![Game](https://img.shields.io/badge/game-arcade-orange.svg)

## 🎯 Game Description

Bubble Bobble is a classic platform arcade game where players control cute dragons (Bub and Bob) who must clear each level by trapping enemies in bubbles and then bursting them. This Python implementation captures the essence of the original game with:

- **🎮 Cooperative multiplayer gameplay** - Two players can play simultaneously
- **🐲 Dragon characters** with unique abilities to shoot bubbles
- **👾 Various enemies** with AI-driven movement patterns
- **🫧 Bubble mechanics** for trapping and defeating enemies
- **🏆 Scoring system** with bonus collectibles
- **⏰ Time-based challenges** with countdown mechanics
- **🏗️ Platform-based level design** with physics simulation

## ✨ Key Features

### 🎪 Gameplay Features
- **Two-player cooperative mode** using different control schemes
- **Physics-based movement** with gravity and collision detection
- **Enemy AI** with pathfinding and direction changes
- **Bubble projectile system** for capturing enemies
- **Score tracking** and bonus collection mechanics
- **Lives system** with respawn functionality
- **Win/lose conditions** based on time and enemy elimination

### 🔧 Technical Features
- **Object-oriented architecture** with clean separation of concerns
- **Actor-based game engine** for flexible entity management
- **Sprite-based graphics** with animated characters
- **Collision detection system** using bounding box algorithms
- **File-based level configuration** for easy level design
- **Modular graphics engine** supporting different rendering backends

## 🏗️ Architecture Overview

The game follows a clean **Model-View-Controller (MVC)** architecture:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   View Layer    │    │ Controller Layer│    │  Model Layer    │
│                 │    │                 │    │                 │
│ boardgui_       │◄──►│ BubbleGui       │◄──►│ BubbleGame      │
│ bubble_bobble   │    │ (Input/Render)  │    │ (Game Logic)    │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                                ┌─────────────────┐
                                                │ Actor System    │
                                                │                 │
                                                │ • Arena         │
                                                │ • Dragon        │
                                                │ • Enemy         │
                                                │ • Bubble        │
                                                │ • Platform      │
                                                │ • Bonus         │
                                                └─────────────────┘
```

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.6+** 🐍
- **Pygame** (for graphics rendering)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GiorCocc/bubble-bobble.git
   cd bubble-bobble
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python boardgui_bubble_bobble.py
   ```

## 🎮 How to Play

### Controls

#### Player 1 (Dragon 1) 🐲
- **W** - Jump/Move up
- **A** - Move left
- **D** - Move right
- **S** - Shoot bubble

#### Player 2 (Dragon 2) 🐲
- **↑** - Jump/Move up
- **←** - Move left
- **→** - Move right
- **↓** - Shoot bubble

### Gameplay Objectives

1. **🎯 Primary Goal:** Eliminate all enemies by trapping them in bubbles
2. **⏰ Time Limit:** Complete levels before time runs out
3. **🏆 Bonus Points:** Collect bonus items for extra score
4. **💖 Lives:** Avoid enemy contact to preserve lives
5. **🏅 Win Condition:** Clear all enemies and collect all bonuses

### Game Mechanics

- **Bubble Physics:** Bubbles travel horizontally then rise vertically
- **Enemy Behavior:** Enemies change direction when hitting walls or other enemies
- **Platform Interaction:** All characters respect platform collision
- **Gravity System:** Realistic falling and jumping mechanics

## 📁 Project Structure

```
bubble-bobble/
│
├── 🎮 Core Game Files
│   ├── bubble_bobble.py           # Game entities (Dragon, Enemy, Bubble, etc.)
│   ├── boardgame_bubble_bobble.py # Game logic and state management
│   ├── boardgui_bubble_bobble.py  # GUI and user interface
│   └── actor.py                   # Base Actor interface and Arena
│
├── 🎨 Graphics & Assets
│   ├── bubble_bobble.png          # Sprite sheet for all graphics
│   ├── g2d.py                     # Web-based graphics engine
│   └── g2d_pyg.py                 # Pygame graphics engine
│
├── 📊 Level Data
│   ├── platform.txt               # Platform positions and dimensions
│   ├── dragon.txt                 # Player starting positions
│   ├── enemy.txt                  # Enemy spawn locations
│   └── bonus.txt                  # Bonus item placements
│
├── 🧪 Testing
│   └── test.py                    # Unit tests for game components
│
└── 📝 Documentation
    └── README.md                  # This file
```

## 🔧 Key Components

### 🏛️ Actor System (`actor.py`)

The foundation of the game engine:

- **`Actor`** - Abstract base class for all game entities
- **`Arena`** - Game world manager handling physics and collisions

```python
class Actor:
    def move(self):        # Called each frame for movement
    def collide(self, other): # Called when collision occurs
    def position(self):    # Returns bounding box
    def symbol(self):      # Returns sprite coordinates
```

### 🐲 Game Entities (`bubble_bobble.py`)

Core game characters and objects:

- **`Dragon`** - Player character with movement and bubble shooting
- **`Enemy`** - AI-controlled opponents with pathfinding
- **`Bubble`** - Projectiles for capturing enemies
- **`Platform`** - Static level geometry
- **`Bonus`** - Collectible score items

### 🎯 Game Logic (`boardgame_bubble_bobble.py`)

Central game state management:

- **Level loading** from configuration files
- **Win/lose condition** evaluation
- **Score tracking** and time management
- **Entity lifecycle** management

### 🖼️ Graphics Engine (`g2d*.py`)

Flexible rendering system:

- **Cross-platform support** (Web and Desktop)
- **Sprite management** with coordinate mapping
- **Input handling** for keyboard controls
- **Canvas rendering** with collision visualization

## 🎨 Graphics & Sprites

The game uses a single sprite sheet (`bubble_bobble.png`) containing all visual assets:

- **Dragon sprites** with directional animations
- **Enemy sprites** with movement states
- **Bubble animations** and effects
- **Platform textures** and decorations
- **Bonus item** graphics

Sprite coordinates are defined in each actor's `symbol()` method for efficient rendering.

## 🧪 Testing

Run the test suite to verify game mechanics:

```bash
python test.py
```

Tests cover:
- **Dragon movement** and collision detection
- **Entity interactions** and physics
- **Arena management** and actor lifecycle

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🔧 Development Setup

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests:**
   ```bash
   python test.py
   ```
5. **Commit and push:**
   ```bash
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```
6. **Create a Pull Request**

### 📝 Contribution Guidelines

- **Code Style:** Follow PEP 8 Python style guidelines
- **Documentation:** Update docstrings and comments
- **Testing:** Add tests for new features
- **Compatibility:** Ensure Python 3.6+ compatibility

### 🎯 Areas for Contribution

- **🆕 New Levels:** Create additional level configurations
- **🎨 Graphics:** Improve sprites and visual effects
- **🔊 Audio:** Add sound effects and music
- **🤖 AI:** Enhance enemy behavior patterns
- **🏆 Features:** Implement power-ups and special abilities
- **⚡ Performance:** Optimize rendering and physics

## 📋 Technical Details

### Dependencies

```
pygame>=2.0.0    # Graphics and input handling
python>=3.6      # Core language support
```

### Performance Characteristics

- **Frame Rate:** 30 FPS game loop
- **Resolution:** 480x420 pixels
- **Memory Usage:** < 50MB typical
- **CPU Usage:** Low (optimized collision detection)

### Platform Compatibility

- **✅ Windows** (Python 3.6+)
- **✅ macOS** (Python 3.6+)
- **✅ Linux** (Python 3.6+)
- **⚠️ Web** (via g2d.py module, experimental)

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

### 📜 License Summary

- **✅ Commercial use**
- **✅ Modification**
- **✅ Distribution**
- **✅ Private use**
- **❌ Liability**
- **❌ Warranty**

## 🎉 Acknowledgments

- **🎮 Original Game:** Taito Corporation (1986)
- **👨‍💻 Framework:** Michele Tomaiuolo's g2d engine
- **🎨 Inspiration:** Classic arcade gaming community
- **🤝 Contributors:** All project contributors

## 🏆 Fun Facts

- **🕹️ Original Release:** Bubble Bobble was first released in 1986
- **🌟 Legacy:** Spawned numerous sequels and remakes
- **🎵 Music:** Famous for its catchy soundtrack
- **👥 Multiplayer:** Pioneer in cooperative arcade gaming
- **🏅 Cultural Impact:** Influenced platform game design for decades

---

**🎮 Happy Gaming!** Enjoy playing this Python recreation of the beloved classic! 🐲🫧

*Built with ❤️ and Python*