#### 一、背景介绍  
Minecraft（《我的世界》）是一款以方块为核心的沙盒游戏，玩家可以通过放置、破坏不同类型的方块（如草方块、石头方块）来构建世界。每个方块有独特的属性（如硬度、透明度）和交互逻辑（如草方块易破坏，石头方块需工具破坏），玩家作为实体可以与这些方块进行互动。  

本练习将通过面向对象编程（OOP）模拟这一过程，帮助理解**封装、继承、多态**在实际场景中的应用：用类封装方块的属性和行为，用继承复用通用逻辑，用多态体现不同方块的差异化交互。


#### 二、要实现的功能  
1. **方块基础行为**：所有方块可被放置（`place()`）和破坏（`break_block()`），并能通过方法获取名称和硬度。  
2. **方块差异化**：  
   - 草方块（`GrassBlock`）：硬度低，易破坏，自带“有草”属性。  
   - 石头方块（`StoneBlock`）：硬度高，需工具破坏。  
3. **玩家交互**：玩家（`Player`）可与任意方块互动，调用方块的破坏方法，体现不同方块的破坏逻辑（多态）。  


#### 三、核心属性（Property）说明  
| 类名          | 私有属性                | 说明                                  | 公共方法（访问/操作属性）                |  
|---------------|-------------------------|---------------------------------------|-----------------------------------------|  
| `Block`       | `_name`                 | 方块名称（如"grass"、"stone"）        | `get_name()`：返回方块名称              |  
|               | `_hardness`             | 硬度值（草方块0.6，石头方块1.5）       | `get_hardness()`：返回硬度值            |  
|               | `_is_transparent`       | 是否透明（草方块和石头均为`False`）    | （无需单独方法，内部逻辑使用）          |  
| `GrassBlock`  | `_has_grass`            | 特有属性，标记是否有草（固定为`True`） | `has_grass()`：返回`_has_grass`的值     |  
| `StoneBlock`  | （无特有私有属性）      | 继承`Block`的所有属性                 | （复用父类方法）                        |  
| `Player`      | （无私有属性）          | 实体类，负责与方块交互                | `interact_with_block(block)`：调用方块的破坏方法 |  


#### 四、基础代码框架（请补充完整）  

##### 1. 基础类 `Block`  
```python
class Block:
    def __init__(self, name, hardness, is_transparent):
        # 初始化私有属性：_name、_hardness、_is_transparent
        pass

    def get_name(self):
        # 返回 _name 的值
        pass

    def get_hardness(self):
        # 返回 _hardness 的值
        pass

    def break_block(self):
        # 打印："破坏方块 {_name}，硬度为 {_hardness}"
        pass

    def place(self):
        # 打印："放置了方块 {_name}"
        pass
```

##### 2. 子类 `GrassBlock` 和 `StoneBlock`  
```python
class GrassBlock(Block):
    def __init__(self):
        # 调用父类 __init__，参数：name="grass"、hardness=0.6、is_transparent=False
        # 定义私有属性 _has_grass = True
        pass

    def break_block(self):
        # 重写：打印"破坏草方块，很容易破坏！（硬度低）"
        pass

    def has_grass(self):
        # 返回 _has_grass 的值
        pass


class StoneBlock(Block):
    def __init__(self):
        # 调用父类 __init__，参数：name="stone"、hardness=1.5、is_transparent=False
        pass

    def break_block(self):
        # 重写：打印"破坏石头方块，需要工具！（硬度高）"
        pass
```

##### 3. 实体类 `Player`  
```python
class Player:
    def interact_with_block(self, block):
        # 调用传入方块的 break_block() 方法（体现多态）
        pass
```


#### 五、测试验证  
运行以下代码，输出应与预期一致：  
```python
grass = GrassBlock()
print("草方块名称：", grass.get_name())  # 预期：草方块名称： grass
grass.place()  # 预期：放置了方块 grass

stone = StoneBlock()
print("石头硬度：", stone.get_hardness())  # 预期：石头硬度： 1.5
stone.place()  # 预期：放置了方块 stone

player = Player()
player.interact_with_block(grass)  # 预期：破坏草方块，很容易破坏！（硬度低）
player.interact_with_block(stone)  # 预期：破坏石头方块，需要工具！（硬度高）

print("草方块是否有草？", grass.has_grass())  # 预期：草方块是否有草？ True
```


---

### 文档 2：Minecraft OOP 练习解决方案  


#### 一、功能实现说明  
本方案通过封装、继承、多态三大OOP特性，实现了Minecraft中方块与玩家的核心交互逻辑：  
- **封装**：用私有属性隐藏方块细节，通过公共方法安全访问。  
- **继承**：草方块和石头方块复用`Block`类的基础行为（放置、属性获取）。  
- **多态**：不同方块重写`break_block()`方法，玩家交互时自动调用对应逻辑。  


