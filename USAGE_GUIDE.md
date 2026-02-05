# 快速使用指南

## 第一步：准备你的输入文件

创建一个Excel文件或CSV文件，格式如下：

| 公司A | 公司B |
|------|------|
| 腾讯控股有限公司 | 腾讯音乐娱乐集团 |
| 阿里巴巴集团 | 阿里云计算有限公司 |
| 百度公司 | 百度在线网络技术有限公司 |

**重要提示：**
- 列名可以是任意名称（程序会自动识别）
- 每一行包含两个公司名称
- 支持 `.xlsx`、`.xls` 和 `.csv` 格式

## 第二步：安装依赖

```bash
pip install -r requirements.txt
```

## 第三步：运行程序

### 最简单的用法

```bash
python3 company_relationship_analyzer.py 你的文件.xlsx
```

结果会自动保存为 `company_relationships_result.xlsx`

### 指定输出文件名

```bash
python3 company_relationship_analyzer.py 你的文件.xlsx -o 结果.xlsx
```

### 测试程序（使用示例文件）

```bash
python3 company_relationship_analyzer.py example_input.csv -o result.xlsx
```

## 第四步：查看结果

打开生成的Excel文件，你会看到：

| 公司A | 公司B | 关联关系 | 查询时间 | 查询状态 |
|------|------|----------|---------|----------|
| 腾讯控股有限公司 | 腾讯音乐娱乐集团 | 未找到直接关联关系 | 2026-02-05 10:30:00 | 成功 |
| 百度公司 | 百度在线网络技术有限公司 | 名称关联：百度在线网络技术有限公司名称包含百度公司 | 2026-02-05 10:30:01 | 成功 |

## 高级用法

### 1. 如果列名不是"公司A"和"公司B"

假设你的Excel有这样的列名：`甲方` 和 `乙方`

```bash
python3 company_relationship_analyzer.py input.xlsx -a "甲方" -b "乙方" -o output.xlsx
```

### 2. 使用第三方API（需要API密钥）

```bash
python3 company_relationship_analyzer.py input.xlsx --api-key YOUR_API_KEY -o output.xlsx
```

**支持的API服务：**
- 企查查 (QCC): https://openapi.qcc.com/
- 天眼查: https://open.tianyancha.com/
- 启信宝: https://www.qixin.com/

## 当前功能说明

### 基础功能（无需API）

程序会自动进行以下分析：

1. **名称包含关系**
   - 检查一个公司名称是否包含另一个
   - 例如："百度在线网络技术有限公司"包含"百度公司"

2. **共同前缀分析**
   - 检测是否有共同的前缀（可能属于同一集团）
   - 例如："华为技术"和"华为云计算"有共同前缀"华为"

### 扩展功能（需要API或自定义）

如果你有企业数据API或数据库，可以扩展查询：
- 投资关系（谁投资了谁）
- 股东关系（共同股东）
- 母子公司关系
- 供应链关系
- 高管任职关系

## 如何扩展程序

如果你想接入真实的企业数据API，编辑 `company_relationship_analyzer.py` 文件的 `_query_via_api` 方法：

```python
def _query_via_api(self, company_a: str, company_b: str) -> List[str]:
    import requests
    
    # 调用你的API
    response = requests.get(
        "https://your-api.com/relationship",
        params={"companyA": company_a, "companyB": company_b},
        headers={"Authorization": f"Bearer {self.api_key}"}
    )
    
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        return data.get("relationships", [])
    
    return []
```

## 常见问题

### Q: 程序说找不到关联关系？
A: 默认情况下，程序只能通过名称匹配找到简单的关联。要获得更详细的关联信息，需要接入企业数据API。

### Q: 支持哪些文件格式？
A: 支持 Excel (.xlsx, .xls) 和 CSV (.csv) 格式。

### Q: 可以处理多少行数据？
A: 理论上没有限制，但如果使用第三方API，要注意API的调用频率限制。

### Q: 查询速度慢怎么办？
A: 
- 基础名称匹配很快
- 如果调用外部API，速度取决于API响应时间
- 可以在代码中添加并发处理来加速

### Q: 结果准确吗？
A: 
- 名称匹配：准确度较低，仅供参考
- API查询：取决于API数据源的质量
- 建议结合多个数据源交叉验证

## 获取帮助

查看所有命令行选项：

```bash
python3 company_relationship_analyzer.py --help
```

## 下一步

1. ✅ 运行示例测试程序
2. ✅ 准备你自己的公司数据文件
3. ✅ 运行程序查看结果
4. ⭕ （可选）集成企业数据API获取更详细的关联信息
5. ⭕ （可选）根据需求定制查询逻辑

祝使用愉快！🎉
