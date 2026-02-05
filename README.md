# 公司关联关系查询程序

这是一个用于查询和分析两个公司之间关联关系的Python程序。

## 功能特点

- ✅ 支持读取Excel (.xlsx, .xls) 和 CSV 文件
- ✅ 自动识别输入文件的列
- ✅ 查询公司之间的关联关系
- ✅ 支持集成第三方API（企查查、天眼查等）
- ✅ 基于名称的智能匹配分析
- ✅ 结果导出为Excel或CSV文件

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 准备输入文件

创建一个Excel或CSV文件，包含两列数据：
- **A列**：第一个公司名称
- **B列**：第二个公司名称

示例 (`example_input.csv`):
```
公司A,公司B
腾讯控股有限公司,腾讯音乐娱乐集团
阿里巴巴集团,阿里云计算有限公司
百度公司,百度在线网络技术有限公司
```

### 2. 运行程序

#### 基本用法

```bash
python company_relationship_analyzer.py input.xlsx -o output.xlsx
```

#### 使用示例文件

```bash
python company_relationship_analyzer.py example_input.csv -o result.xlsx
```

#### 指定列名

```bash
python company_relationship_analyzer.py input.xlsx -o output.xlsx -a "公司名称" -b "关联公司"
```

#### 使用API密钥（如果有第三方API）

```bash
python company_relationship_analyzer.py input.xlsx -o output.xlsx --api-key YOUR_API_KEY
```

### 3. 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `input_file` | 输入文件路径（必需） | - |
| `-o, --output` | 输出文件路径 | `company_relationships_result.xlsx` |
| `-a, --column-a` | 公司A列的列名 | 自动识别第一列 |
| `-b, --column-b` | 公司B列的列名 | 自动识别第二列 |
| `--api-key` | API密钥（可选） | - |

### 4. 查看帮助

```bash
python company_relationship_analyzer.py --help
```

## 输出结果

程序会生成一个包含以下信息的输出文件：

| 列名 | 说明 |
|------|------|
| 公司A | 第一个公司名称 |
| 公司B | 第二个公司名称 |
| 关联关系 | 查询到的关联关系描述 |
| 查询时间 | 查询的时间戳 |
| 查询状态 | 成功或失败 |

## 集成第三方API

程序提供了集成第三方API的框架。如果你有企查查、天眼查或其他商业数据API的访问权限，可以修改 `_query_via_api` 方法来实现实际的API调用。

### 常用API服务

1. **企查查** (QCC)
   - 官网: https://openapi.qcc.com/
   - 提供企业工商信息、股权关系、投资信息等

2. **天眼查** (Tianyancha)
   - 官网: https://open.tianyancha.com/
   - 提供企业关系图谱、股权穿透等功能

3. **启信宝** (Qixin)
   - 官网: https://www.qixin.com/
   - 提供企业关联分析、风险监控等

### API集成示例

在 `company_relationship_analyzer.py` 的 `_query_via_api` 方法中，你可以添加实际的API调用代码：

```python
def _query_via_api(self, company_a: str, company_b: str) -> List[str]:
    import requests
    
    relationships = []
    
    # 查询公司A的信息
    response_a = requests.get(
        "https://api.qcc.com/company/info",
        params={"keyword": company_a},
        headers={"Token": self.api_key}
    )
    
    # 查询公司B的信息
    response_b = requests.get(
        "https://api.qcc.com/company/info",
        params={"keyword": company_b},
        headers={"Token": self.api_key}
    )
    
    # 分析关联关系
    if response_a.status_code == 200 and response_b.status_code == 200:
        # 处理API返回的数据
        # ...
        
    return relationships
```

## 当前功能

目前程序包含以下分析功能：

1. **名称匹配分析**
   - 检查公司名称的包含关系
   - 识别共同前缀（可能属于同一集团）

2. **API查询框架**
   - 预留了API集成接口
   - 可以方便地接入各种企业数据API

3. **本地数据库查询**
   - 预留了数据库查询接口
   - 可以连接本地企业关系数据库

## 扩展功能

你可以根据需要扩展以下功能：

1. **更多关系类型**
   - 投资关系
   - 股东关系
   - 母子公司关系
   - 供应链关系
   - 竞争关系

2. **数据来源**
   - 连接企业数据库
   - 爬取公开信息
   - 调用商业API
   - 导入Excel数据

3. **可视化**
   - 生成关系图谱
   - 导出网络图
   - 生成报告

## 注意事项

1. 使用第三方API可能需要付费
2. 请遵守相关API的使用条款和限制
3. 建议添加请求延迟，避免请求过于频繁
4. 敏感数据请注意保密

## 示例运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行示例
python company_relationship_analyzer.py example_input.csv -o result.xlsx

# 查看结果
# 结果会保存在 result.xlsx 文件中
```

## 技术支持

如有问题或建议，请提交Issue。

## 许可证

MIT License
