##### 1. 复用基础类 `Block`、`StoneBlock`（来自之前练习）  
```python
class Block:
    def __init__(self, name, hardness, is_transparent):
        self._name = name
        self._hardness = hardness
        self._is_transparent = is_transparent

    def get_name(self):
        return self._name

    def get_hardness(self):
        return self._hardness

    def break_block(self):
        print(f"破坏方块 {self._name}，硬度为 {self._hardness}")

    def place(self):
        print(f"放置了方块 {self._name}")


class StoneBlock(Block):
    def __init__(self):
        super().__init__(name="stone", hardness=1.5, is_transparent=False)

    def break_block(self):
        print("破坏石头方块，需要工具！（硬度高）")
```

##### 2. 特殊特性 Mixin 类  
```python
class LuminousBlock:
    def __init__(self, luminous_level):
        self._luminous_level = luminous_level  # 发光等级

    def emit_light(self):
        # 注意：需通过 get_name() 获取方块名称（依赖基础方块类的方法）
        print(f"{self.get_name()} 发出 {self._luminous_level} 级光芒")

    def get_luminous_level(self):
        return self._luminous_level


class FarmableBlock:
    def __init__(self, is_farmable):
        self._is_farmable = is_farmable  # 是否可种植

    def plant_crop(self):
        if self._is_farmable:
            print(f"在 {self.get_name()} 上种植了作物")
        else:
            print("该方块不可种植")

    def is_farmable(self):
        return self._is_farmable
```

##### 3. 新增基础方块类 `DirtBlock`  
```python
class DirtBlock(Block):
    def __init__(self):
        super().__init__(name="dirt", hardness=0.5, is_transparent=False)

    def break_block(self):
        print("破坏泥土方块，用手即可轻松破坏")
```

##### 4. 复合方块类（多重继承）  
```python
class LuminousStoneBlock(StoneBlock, LuminousBlock):
    def __init__(self):
        # 初始化第一个父类（StoneBlock）
        StoneBlock.__init__(self)
        # 初始化第二个父类（LuminousBlock）
        LuminousBlock.__init__(self, luminous_level=10)


class FarmableDirtBlock(DirtBlock, FarmableBlock):
    def __init__(self):
        # 初始化第一个父类（DirtBlock）
        DirtBlock.__init__(self)
        # 初始化第二个父类（FarmableBlock）
        FarmableBlock.__init__(self, is_farmable=True)
```

##### 5. 玩家类（支持多重特性交互）  
```python
class Player:
    def interact_with_block(self, block):
        block.break_block()

    def trigger_light(self, block):
        block.emit_light()

    def plant_on_block(self, block):
        block.plant_crop()
```


#### 三、测试结果  
运行测试代码后，输出如下，验证多重继承功能正常：  
```
发光石头名称： stone
发光等级： 10
放置了方块 stone
破坏石头方块，需要工具！（硬度高）
stone 发出 10 级光芒
泥土硬度： 0.5
是否可种植： True
放置了方块 dirt
破坏泥土方块，用手即可轻松破坏
在 dirt 上种植了作物
```


#### 四、多重继承关键点  
1. **Mixin 类设计**：`LuminousBlock` 和 `FarmableBlock` 不直接继承 `Block`，但依赖 `Block` 的方法（如 `get_name()`），仅封装单一特性，提高复用性。  
2. **初始化顺序**：复合类需显式调用所有父类的 `__init__` 方法（如 `StoneBlock.__init__(self)`），否则父类属性不会被初始化。  
3. **方法查找顺序**：若多个父类有同名方法，Python 按“从左到右”顺序查找（如 `LuminousStoneBlock` 优先使用 `StoneBlock` 的方法）。