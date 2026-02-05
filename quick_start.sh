#!/bin/bash
echo "====================================="
echo "公司关联关系查询程序 - 快速启动"
echo "====================================="
echo ""
echo "步骤1: 安装依赖..."
pip3 install -r requirements.txt
echo ""
echo "步骤2: 测试程序..."
python3 company_relationship_analyzer.py example_input.csv -o result.xlsx
echo ""
echo "====================================="
echo "✅ 测试完成！"
echo "📁 结果已保存到: result.xlsx"
echo ""
echo "现在可以使用你自己的文件了："
echo "python3 company_relationship_analyzer.py 你的文件.xlsx -o 输出.xlsx"
echo "====================================="
