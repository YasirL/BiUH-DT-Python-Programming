#### һ����������  
�� Minecraft �У����ַ��鲻�����л������ԣ���Ӳ�ȡ����ƣ���������ͬʱӵ�ж����������ԡ����磺�������ʯͷ���顱������ͨʯͷһ����Ӳ�����������һ�����⣻������ֲ���������顱�ȱ����������������ԣ�����֧��ֲ����ֲ��  

���ࡰ�������ԡ��ķ����ʺ���**���ؼ̳�**ʵ�֣�һ������ͬʱ�̳ж����������Ժͷ����������ظ���д���롣����ϰ��ͨ����ƴ��෽�飬���ն��ؼ̳е��﷨��Ӧ�ó�����  


#### ����Ҫʵ�ֵĹ���  
1. **����������**������֮ǰ�� `Block` �ࣨ�� `_name`��`_hardness` �����Լ� `place()`��`break_block()` �ȷ�������  
2. **�������� Mixin ��**��  
   - `LuminousBlock`�����ⷽ�飩���� `_luminous_level`������ȼ������ԣ��ṩ `emit_light()` ��������ӡ������Ϣ���� `get_luminous_level()` ���������ط���ȼ�����  
   - `FarmableBlock`������ֲ���飩���� `_is_farmable`���Ƿ����ֲ�����ԣ��ṩ `plant_crop()` ��������ӡ��ֲ��Ϣ���� `is_farmable()` �����������Ƿ����ֲ����  
3. **���Ϸ�����**��  
   - `LuminousStoneBlock`��ͬʱ�̳� `StoneBlock`��ʯͷ���飩�� `LuminousBlock`�����ⷽ�飩��ӵ��ʯͷ��Ӳ�Ⱥͷ������ԡ�  
   - `FarmableDirtBlock`��ͬʱ�̳� `DirtBlock`���������飩�� `FarmableBlock`������ֲ���飩��ӵ������������ȺͿ���ֲ���ԡ�  
4. **��ҽ���**����ҿɵ��ø��Ϸ�������м̳з��������ƻ������⡢��ֲ����  


#### �����������������ϵ  
| ����                 | ����                  | ˽������                | ����/��д����                          |  
|----------------------|-----------------------|-------------------------|---------------------------------------|  
| `LuminousBlock`      | �ޣ�Mixin �ࣩ        | `_luminous_level`       | `emit_light()`��`get_luminous_level()` |  
| `FarmableBlock`      | �ޣ�Mixin �ࣩ        | `_is_farmable`          | `plant_crop()`��`is_farmable()`        |  
| `DirtBlock`          | `Block`               | ���̳� `Block` ���ԣ�   | ��д `break_block()`�������������ƻ��� |  
| `LuminousStoneBlock` | `StoneBlock`��`LuminousBlock` | ���̳����и������ԣ� | �����ø��෽��������������             |  
| `FarmableDirtBlock`  | `DirtBlock`��`FarmableBlock` | ���̳����и������ԣ� | �����ø��෽��������������             |  


#### �ġ����������ܣ��벹��������  

##### 1. �������� Mixin ��  
```python
class LuminousBlock:
    def __init__(self, luminous_level):
        # ��ʼ��˽������ _luminous_level������ȼ�����15Ϊ��ߣ�
        pass

    def emit_light(self):
        # ��ӡ��"{��������} ���� {_luminous_level} ����â"
        pass

    def get_luminous_level(self):
        # ���� _luminous_level ��ֵ
        pass


class FarmableBlock:
    def __init__(self, is_farmable):
        # ��ʼ��˽������ _is_farmable���Ƿ����ֲ������ֵ��
        pass

    def plant_crop(self):
        # ��ӡ��"�� {��������} ����ֲ������"����������ֲ����ӡ"�÷��鲻����ֲ"��
        pass

    def is_farmable(self):
        # ���� _is_farmable ��ֵ
        pass
```

##### 2. �������������� `DirtBlock`  
```python
class DirtBlock(Block):
    def __init__(self):
        # ���ø��� __init__��������name="dirt"��hardness=0.5��is_transparent=False
        pass

    def break_block(self):
        # ��д����ӡ"�ƻ��������飬���ּ��������ƻ�"
        pass
```

##### 3. ���Ϸ����ࣨ���ؼ̳У�  
```python
class LuminousStoneBlock(StoneBlock, LuminousBlock):
    def __init__(self):
        # ���� StoneBlock ����� __init__�����贫�Σ�StoneBlock �ѹ̶����ԣ�
        # ���� LuminousBlock ����� __init__��������luminous_level=10
        pass


class FarmableDirtBlock(DirtBlock, FarmableBlock):
    def __init__(self):
        # ���� DirtBlock ����� __init__�����贫�Σ�DirtBlock �ѹ̶����ԣ�
        # ���� FarmableBlock ����� __init__��������is_farmable=True
        pass
```

##### 4. ����ࣨ����֮ǰ�� `Player`����������������  
```python
class Player:
    # ����֮ǰ�� interact_with_block ����
    def interact_with_block(self, block):
        block.break_block()

    # �������������鷢�⣨���� LuminousBlock ������Ч��
    def trigger_light(self, block):
        block.emit_light()

    # �������ڷ�������ֲ������ FarmableBlock ������Ч��
    def plant_on_block(self, block):
        block.plant_crop()
```


#### �塢������֤  
�������´��룬���Ӧ��Ԥ��һ�£�  
```python
# ���Է���ʯͷ����
luminous_stone = LuminousStoneBlock()
print("����ʯͷ���ƣ�", luminous_stone.get_name())  # Ԥ�ڣ�����ʯͷ���ƣ� stone
print("����ȼ���", luminous_stone.get_luminous_level())  # Ԥ�ڣ�����ȼ��� 10
luminous_stone.place()  # Ԥ�ڣ������˷��� stone
player = Player()
player.interact_with_block(luminous_stone)  # Ԥ�ڣ��ƻ�ʯͷ���飬��Ҫ���ߣ���Ӳ�ȸߣ�
player.trigger_light(luminous_stone)  # Ԥ�ڣ�stone ���� 10 ����â

# ���Կ���ֲ��������
farmable_dirt = FarmableDirtBlock()
print("����Ӳ�ȣ�", farmable_dirt.get_hardness())  # Ԥ�ڣ�����Ӳ�ȣ� 0.5
print("�Ƿ����ֲ��", farmable_dirt.is_farmable())  # Ԥ�ڣ��Ƿ����ֲ�� True
farmable_dirt.place()  # Ԥ�ڣ������˷��� dirt
player.interact_with_block(farmable_dirt)  # Ԥ�ڣ��ƻ��������飬���ּ��������ƻ�
player.plant_on_block(farmable_dirt)  # Ԥ�ڣ��� dirt ����ֲ������
```


---

### �ĵ� 2��Minecraft ���ؼ̳���ϰ�������  


#### һ��ʵ��˵��  
������ͨ�����ؼ̳�ʵ�֡��������Է��顱�������߼���  
- �� **Mixin ��**��`LuminousBlock`��`FarmableBlock`����װ��һ�������ԣ��������ิ�á�  
- ���Ϸ����ࣨ`LuminousStoneBlock`��`FarmableDirtBlock`��ͬʱ�̳л���������� Mixin �࣬һ���Ի�ö������ԡ�  
- ���ؼ̳��У�ͨ����ʽ���ø��� `__init__` ������ʼ�����и�������ԣ��������Զ�ʧ��  


