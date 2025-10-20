#### 一、背景介绍  
在 Minecraft 中，部分方块不仅具有基础属性（如硬度、名称），还可能同时拥有多种特殊特性。例如：“发光的石头方块”既像普通石头一样坚硬，又能像灯笼一样发光；“可种植的泥土方块”既保留泥土的松软特性，又能支持植物种植。  

这类“复合特性”的方块适合用**多重继承**实现：一个子类同时继承多个父类的属性和方法，无需重复编写代码。本练习将通过设计此类方块，掌握多重继承的语法和应用场景。  


#### 二、要实现的功能  
1. **基础方块类**：保留之前的 `Block` 类（含 `_name`、`_hardness` 等属性及 `place()`、`break_block()` 等方法）。  
2. **特殊特性 Mixin 类**：  
   - `LuminousBlock`（发光方块）：含 `_luminous_level`（发光等级）属性，提供 `emit_light()` 方法（打印发光信息）和 `get_luminous_level()` 方法（返回发光等级）。  
   - `FarmableBlock`（可种植方块）：含 `_is_farmable`（是否可种植）属性，提供 `plant_crop()` 方法（打印种植信息）和 `is_farmable()` 方法（返回是否可种植）。  
3. **复合方块类**：  
   - `LuminousStoneBlock`：同时继承 `StoneBlock`（石头方块）和 `LuminousBlock`（发光方块），拥有石头的硬度和发光特性。  
   - `FarmableDirtBlock`：同时继承 `DirtBlock`（泥土方块）和 `FarmableBlock`（可种植方块），拥有泥土的松软度和可种植特性。  
4. **玩家交互**：玩家可调用复合方块的所有继承方法（如破坏、发光、种植）。  


#### 三、核心属性与类关系  
| 类名                 | 父类                  | 私有属性                | 新增/重写方法                          |  
|----------------------|-----------------------|-------------------------|---------------------------------------|  
| `LuminousBlock`      | 无（Mixin 类）        | `_luminous_level`       | `emit_light()`、`get_luminous_level()` |  
| `FarmableBlock`      | 无（Mixin 类）        | `_is_farmable`          | `plant_crop()`、`is_farmable()`        |  
| `DirtBlock`          | `Block`               | （继承 `Block` 属性）   | 重写 `break_block()`（体现泥土易破坏） |  
| `LuminousStoneBlock` | `StoneBlock`、`LuminousBlock` | （继承所有父类属性） | （复用父类方法，无需新增）             |  
| `FarmableDirtBlock`  | `DirtBlock`、`FarmableBlock` | （继承所有父类属性） | （复用父类方法，无需新增）             |  


#### 四、基础代码框架（请补充完整）  

##### 1. 特殊特性 Mixin 类  
```python
class LuminousBlock:
    def __init__(self, luminous_level):
        # 初始化私有属性 _luminous_level（发光等级，如15为最高）
        pass

    def emit_light(self):
        # 打印："{方块名称} 发出 {_luminous_level} 级光芒"
        pass

    def get_luminous_level(self):
        # 返回 _luminous_level 的值
        pass


class FarmableBlock:
    def __init__(self, is_farmable):
        # 初始化私有属性 _is_farmable（是否可种植，布尔值）
        pass

    def plant_crop(self):
        # 打印："在 {方块名称} 上种植了作物"（若不可种植，打印"该方块不可种植"）
        pass

    def is_farmable(self):
        # 返回 _is_farmable 的值
        pass
```

##### 2. 新增基础方块类 `DirtBlock`  
```python
class DirtBlock(Block):
    def __init__(self):
        # 调用父类 __init__，参数：name="dirt"、hardness=0.5、is_transparent=False
        pass

    def break_block(self):
        # 重写：打印"破坏泥土方块，用手即可轻松破坏"
        pass
```

##### 3. 复合方块类（多重继承）  
```python
class LuminousStoneBlock(StoneBlock, LuminousBlock):
    def __init__(self):
        # 调用 StoneBlock 父类的 __init__（无需传参，StoneBlock 已固定属性）
        # 调用 LuminousBlock 父类的 __init__，参数：luminous_level=10
        pass


class FarmableDirtBlock(DirtBlock, FarmableBlock):
    def __init__(self):
        # 调用 DirtBlock 父类的 __init__（无需传参，DirtBlock 已固定属性）
        # 调用 FarmableBlock 父类的 __init__，参数：is_farmable=True
        pass
```

##### 4. 玩家类（复用之前的 `Player`，新增交互方法）  
```python
class Player:
    # 复用之前的 interact_with_block 方法
    def interact_with_block(self, block):
        block.break_block()

    # 新增：触发方块发光（仅对 LuminousBlock 子类有效）
    def trigger_light(self, block):
        block.emit_light()

    # 新增：在方块上种植（仅对 FarmableBlock 子类有效）
    def plant_on_block(self, block):
        block.plant_crop()
```


#### 五、测试验证  
运行以下代码，输出应与预期一致：  
```python
# 测试发光石头方块
luminous_stone = LuminousStoneBlock()
print("发光石头名称：", luminous_stone.get_name())  # 预期：发光石头名称： stone
print("发光等级：", luminous_stone.get_luminous_level())  # 预期：发光等级： 10
luminous_stone.place()  # 预期：放置了方块 stone
player = Player()
player.interact_with_block(luminous_stone)  # 预期：破坏石头方块，需要工具！（硬度高）
player.trigger_light(luminous_stone)  # 预期：stone 发出 10 级光芒

# 测试可种植泥土方块
farmable_dirt = FarmableDirtBlock()
print("泥土硬度：", farmable_dirt.get_hardness())  # 预期：泥土硬度： 0.5
print("是否可种植：", farmable_dirt.is_farmable())  # 预期：是否可种植： True
farmable_dirt.place()  # 预期：放置了方块 dirt
player.interact_with_block(farmable_dirt)  # 预期：破坏泥土方块，用手即可轻松破坏
player.plant_on_block(farmable_dirt)  # 预期：在 dirt 上种植了作物
```


---

### 文档 2：Minecraft 多重继承练习解决方案  


#### 一、实现说明  
本方案通过多重继承实现“复合特性方块”，核心逻辑：  
- 用 **Mixin 类**（`LuminousBlock`、`FarmableBlock`）封装单一特殊特性，供其他类复用。  
- 复合方块类（`LuminousStoneBlock`、`FarmableDirtBlock`）同时继承基础方块类和 Mixin 类，一次性获得多种特性。  
- 多重继承中，通过显式调用父类 `__init__` 方法初始化所有父类的属性，避免属性丢失。  


