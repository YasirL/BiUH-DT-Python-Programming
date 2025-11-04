##### 1. 基础类 `Block`（封装核心属性与方法）  
```python
class Block:
    def __init__(self, name, hardness, is_transparent):
        self._name = name  # 封装：方块名称（私有属性）
        self._hardness = hardness  # 封装：硬度（私有属性）
        self._is_transparent = is_transparent  # 封装：透明度（私有属性）

    def get_name(self):
        return self._name  # 公共方法：访问名称

    def get_hardness(self):
        return self._hardness  # 公共方法：访问硬度

    def break_block(self):
        print(f"破坏方块 {self._name}，硬度为 {self._hardness}")  # 基础破坏逻辑

    def place(self):
        print(f"放置了方块 {self._name}")  # 基础放置逻辑
```

##### 2. 子类 `GrassBlock`（继承+扩展）  
```python
class GrassBlock(Block):
    def __init__(self):
        # 继承：调用父类构造方法初始化公共属性
        super().__init__(name="grass", hardness=0.6, is_transparent=False)
        self._has_grass = True  # 封装：子类特有属性（是否有草）

    def break_block(self):
        # 多态：重写破坏方法，体现草方块特性
        print("破坏草方块，很容易破坏！（硬度低）")

    def has_grass(self):
        return self._has_grass  # 公共方法：访问子类特有属性
```

##### 3. 子类 `StoneBlock`（继承+重写）  
```python
class StoneBlock(Block):
    def __init__(self):
        # 继承：调用父类构造方法初始化公共属性
        super().__init__(name="stone", hardness=1.5, is_transparent=False)

    def break_block(self):
        # 多态：重写破坏方法，体现石头方块特性
        print("破坏石头方块，需要工具！（硬度高）")
```

##### 4. 实体类 `Player`（多态调用）  
```python
class Player:
    def interact_with_block(self, block):
        # 多态核心：传入不同方块时，自动调用对应子类的 break_block()
        block.break_block()
```


#### 三、测试结果  
运行测试代码后，输出如下，验证所有功能正常：  
```
草方块名称： grass
放置了方块 grass
石头硬度： 1.5
放置了方块 stone
破坏草方块，很容易破坏！（硬度低）
破坏石头方块，需要工具！（硬度高）
草方块是否有草？ True
```


#### 四、属性与特性对应关系  
| 属性/方法               | 关联OOP特性       | 作用说明                                  |  
|-------------------------|------------------|-------------------------------------------|  
| `_name`、`_hardness`等  | 封装             | 隐藏内部数据，仅通过`get_name()`等方法访问 |  
| `GrassBlock(Block)`     | 继承             | 复用`Block`的`place()`等基础方法          |  
| `GrassBlock.break_block()` | 多态           | 重写父类方法，体现草方块的破坏逻辑        |  
| `Player.interact_with_block()` | 多态        | 统一调用入口，适配不同方块的破坏行为      |