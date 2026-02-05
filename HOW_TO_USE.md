# 如何使用公司关联关系查询程序

## 🚀 三分钟快速上手

### 1️⃣ 准备输入文件

在Excel中创建一个表格：

```
列A          |  列B
-------------|-------------
腾讯控股     | 腾讯音乐
阿里巴巴     | 阿里云
```

保存为 `my_companies.xlsx`

### 2️⃣ 运行程序

打开终端，进入程序所在目录，执行：

```bash
python3 company_relationship_analyzer.py my_companies.xlsx -o 结果.xlsx
```

### 3️⃣ 查看结果

打开生成的 `结果.xlsx` 文件，查看分析结果！

---

## 📖 详细使用说明

### 命令格式

```bash
python3 company_relationship_analyzer.py <输入文件> [选项]
```

### 必需参数

- `<输入文件>` - 包含公司名称的Excel或CSV文件路径

### 可选参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-o`, `--output` | 输出文件路径 | `-o result.xlsx` |
| `-a`, `--column-a` | A列的列名 | `-a "甲方"` |
| `-b`, `--column-b` | B列的列名 | `-b "乙方"` |
| `--api-key` | API密钥 | `--api-key abc123` |

---

## 💼 实际使用场景

### 场景1：标准Excel文件

你有一个 `companies.xlsx`，列名是"公司A"和"公司B"：

```bash
python3 company_relationship_analyzer.py companies.xlsx
```

结果自动保存为 `company_relationships_result.xlsx`

### 场景2：CSV文件

你有一个 `data.csv` 文件：

```bash
python3 company_relationship_analyzer.py data.csv -o 分析结果.xlsx
```

### 场景3：自定义列名

你的Excel列名是"母公司"和"子公司"：

```bash
python3 company_relationship_analyzer.py file.xlsx -a "母公司" -b "子公司" -o output.xlsx
```

### 场景4：批量处理

处理多个文件：

```bash
python3 company_relationship_analyzer.py file1.xlsx -o result1.xlsx
python3 company_relationship_analyzer.py file2.xlsx -o result2.xlsx
python3 company_relationship_analyzer.py file3.xlsx -o result3.xlsx
```

---

## 📝 输入文件要求

### Excel格式 (.xlsx, .xls)

```
| 公司A              | 公司B                    |
|--------------------|--------------------------|
| 腾讯控股有限公司   | 腾讯音乐娱乐集团         |
| 阿里巴巴集团       | 阿里云计算有限公司       |
```

### CSV格式 (.csv)

```csv
公司A,公司B
腾讯控股有限公司,腾讯音乐娱乐集团
阿里巴巴集团,阿里云计算有限公司
```

### 重要提示

- ✅ 至少需要两列
- ✅ 列名可以任意（程序会自动识别）
- ✅ 公司名称不能为空
- ✅ 支持中文、英文公司名
- ❌ 不支持合并单元格

---

## 🎯 运行效果示例

运行程序后，你会看到类似的输出：

```
============================================================
公司关联关系查询程序
============================================================
成功读取文件: my_companies.xlsx
数据行数: 10

开始分析 10 对公司关系...
============================================================

第 1 行: 查询 '腾讯控股有限公司' 和 '腾讯音乐娱乐集团' 的关系...
  └─ 可能的关联：共同前缀 '腾讯'，可能属于同一集团

第 2 行: 查询 '阿里巴巴集团' 和 '阿里云计算有限公司' 的关系...
  └─ 名称关联：阿里云计算有限公司名称包含阿里

...

============================================================
分析完成！共处理 10 对公司关系

结果已保存到: result.xlsx

程序执行完成！
```

---

## 📊 输出结果说明

生成的Excel文件包含以下列：

| 列名 | 说明 | 示例 |
|------|------|------|
| 公司A | 第一个公司 | 腾讯控股有限公司 |
| 公司B | 第二个公司 | 腾讯音乐娱乐集团 |
| 关联关系 | 查询到的关系 | 可能的关联：共同前缀 '腾讯' |
| 查询时间 | 查询时间戳 | 2026-02-05 10:30:00 |
| 查询状态 | 成功/失败 | 成功 |

---

## 🔍 当前可识别的关系类型

### 1. 名称包含关系

```
输入: "百度公司" vs "百度在线网络技术有限公司"
输出: 名称关联：百度在线网络技术有限公司名称包含百度公司
```

### 2. 共同前缀（同一集团）

```
输入: "华为技术有限公司" vs "华为云计算技术有限公司"
输出: 可能的关联：共同前缀 '华为'，可能属于同一集团
```

### 3. 未找到关联

```
输入: "苹果公司" vs "微软公司"
输出: 未找到直接关联关系
```

---

## ⚠️ 常见问题

### 问题1: 提示"command not found: python3"

**解决**：尝试使用 `python` 而不是 `python3`
```bash
python company_relationship_analyzer.py input.xlsx
```

### 问题2: 提示"No module named 'pandas'"

**解决**：先安装依赖
```bash
pip3 install -r requirements.txt
```

### 问题3: 结果都是"未找到关联关系"

**原因**：程序默认只能识别简单的名称匹配

**解决**：需要接入企业数据API（如企查查、天眼查）来获取真实的关联关系

### 问题4: 文件路径有空格

**解决**：用引号包裹文件路径
```bash
python3 company_relationship_analyzer.py "我的文件 2024.xlsx" -o "结果 2024.xlsx"
```

### 问题5: 列名识别错误

**解决**：手动指定列名
```bash
python3 company_relationship_analyzer.py input.xlsx -a "第一列名" -b "第二列名"
```

---

## 🎓 从零开始完整示例

假设你是第一次使用，完整步骤如下：

```bash
# 1. 进入程序目录
cd /path/to/company_relationship_analyzer

# 2. 安装依赖（只需一次）
pip3 install -r requirements.txt

# 3. 测试程序（使用示例文件）
python3 company_relationship_analyzer.py example_input.csv -o test.xlsx

# 4. 检查 test.xlsx 文件，确认程序正常工作

# 5. 使用你自己的文件
python3 company_relationship_analyzer.py 你的文件.xlsx -o 结果.xlsx

# 6. 打开结果文件查看分析结果
```

---

## 🚀 下一步

1. ✅ 使用示例文件测试程序
2. ✅ 准备你的公司清单
3. ✅ 运行程序查看结果
4. ⭕ （可选）修改代码接入企业数据API
5. ⭕ （可选）根据需求定制分析逻辑

---

## 📞 获取更多帮助

```bash
# 查看所有命令行选项
python3 company_relationship_analyzer.py --help

# 查看程序版本和说明
head -n 20 company_relationship_analyzer.py
```

---

## ✨ 提示

- 💡 程序会自动去除"有限公司"、"股份有限公司"等后缀进行匹配
- 💡 如果两个公司有3个字以上的共同前缀，程序会提示可能属于同一集团
- 💡 处理大量数据时，建议先用小数据集测试
- 💡 CSV文件建议使用UTF-8编码保存

祝使用愉快！🎉
