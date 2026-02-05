#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公司关联关系查询程序
用于查询两个公司之间的关联关系
"""

import pandas as pd
import os
import json
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import argparse


class CompanyRelationshipAnalyzer:
    """公司关联关系分析器"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化分析器
        
        Args:
            api_key: API密钥（如果使用第三方API）
        """
        self.api_key = api_key
        self.results = []
    
    def read_input_file(self, file_path: str) -> pd.DataFrame:
        """
        读取输入文件（支持Excel和CSV）
        
        Args:
            file_path: 文件路径
            
        Returns:
            DataFrame包含公司数据
        """
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path)
            elif file_ext == '.csv':
                df = pd.read_csv(file_path, encoding='utf-8-sig')
            else:
                raise ValueError(f"不支持的文件格式: {file_ext}，请使用 .xlsx, .xls 或 .csv 文件")
            
            print(f"成功读取文件: {file_path}")
            print(f"数据行数: {len(df)}")
            return df
        except Exception as e:
            raise Exception(f"读取文件失败: {str(e)}")
    
    def query_relationship(self, company_a: str, company_b: str) -> Dict:
        """
        查询两个公司之间的关联关系
        
        Args:
            company_a: 公司A名称
            company_b: 公司B名称
            
        Returns:
            包含关联关系信息的字典
        """
        # 这里实现查询逻辑
        # 可以调用企查查、天眼查等API，或查询本地数据库
        
        relationship_info = {
            '公司A': company_a,
            '公司B': company_b,
            '关联关系': [],
            '查询时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            '查询状态': '成功'
        }
        
        # 示例：检查常见的关联关系类型
        relationships = self._check_relationships(company_a, company_b)
        relationship_info['关联关系'] = relationships
        
        if not relationships:
            relationship_info['关联关系'] = ['未找到直接关联关系']
        
        return relationship_info
    
    def _check_relationships(self, company_a: str, company_b: str) -> List[str]:
        """
        检查各种可能的关联关系
        
        Args:
            company_a: 公司A名称
            company_b: 公司B名称
            
        Returns:
            关联关系列表
        """
        relationships = []
        
        # 方法1: 调用第三方API（需要API密钥）
        # 例如：企查查、天眼查、启信宝等
        if self.api_key:
            api_relationships = self._query_via_api(company_a, company_b)
            relationships.extend(api_relationships)
        
        # 方法2: 基于名称的简单匹配（作为示例）
        simple_match = self._simple_name_matching(company_a, company_b)
        if simple_match:
            relationships.append(simple_match)
        
        # 方法3: 从本地数据库查询（如果有）
        # db_relationships = self._query_from_database(company_a, company_b)
        # relationships.extend(db_relationships)
        
        return relationships
    
    def _query_via_api(self, company_a: str, company_b: str) -> List[str]:
        """
        通过API查询关联关系
        
        注意：这是一个示例框架，需要替换为实际的API调用
        常用API：
        - 企查查: https://openapi.qcc.com/
        - 天眼查: https://open.tianyancha.com/
        - 启信宝: https://www.qixin.com/
        """
        relationships = []
        
        # TODO: 实现实际的API调用
        # 示例代码结构：
        # import requests
        # 
        # # 查询公司A的信息
        # response_a = requests.get(
        #     f"https://api.example.com/company/info",
        #     params={"name": company_a},
        #     headers={"Authorization": f"Bearer {self.api_key}"}
        # )
        # 
        # # 查询公司B的信息
        # response_b = requests.get(
        #     f"https://api.example.com/company/info",
        #     params={"name": company_b},
        #     headers={"Authorization": f"Bearer {self.api_key}"}
        # )
        # 
        # # 分析关联关系
        # if response_a.status_code == 200 and response_b.status_code == 200:
        #     data_a = response_a.json()
        #     data_b = response_b.json()
        #     
        #     # 检查投资关系
        #     if self._check_investment(data_a, data_b):
        #         relationships.append("投资关系")
        #     
        #     # 检查股东关系
        #     if self._check_shareholder(data_a, data_b):
        #         relationships.append("股东关系")
        #     
        #     # 检查母子公司关系
        #     if self._check_parent_subsidiary(data_a, data_b):
        #         relationships.append("母子公司关系")
        
        return relationships
    
    def _simple_name_matching(self, company_a: str, company_b: str) -> Optional[str]:
        """
        基于名称的简单匹配分析
        """
        # 去除常见的公司后缀
        suffixes = ['有限公司', '股份有限公司', '集团', '公司', 'Co.,Ltd', 'Ltd', 'Inc']
        
        name_a = company_a
        name_b = company_b
        
        for suffix in suffixes:
            name_a = name_a.replace(suffix, '')
            name_b = name_b.replace(suffix, '')
        
        name_a = name_a.strip()
        name_b = name_b.strip()
        
        # 检查名称包含关系
        if name_a in name_b:
            return f"名称关联：{company_b}名称包含{company_a}"
        elif name_b in name_a:
            return f"名称关联：{company_a}名称包含{company_b}"
        
        # 检查共同前缀（可能是同一集团）
        if len(name_a) >= 3 and len(name_b) >= 3:
            common_prefix_len = 0
            for i in range(min(len(name_a), len(name_b))):
                if name_a[i] == name_b[i]:
                    common_prefix_len += 1
                else:
                    break
            
            if common_prefix_len >= 3:
                return f"可能的关联：共同前缀 '{name_a[:common_prefix_len]}'，可能属于同一集团"
        
        return None
    
    def analyze_all(self, df: pd.DataFrame, 
                    column_a: str = 'A列', 
                    column_b: str = 'B列') -> pd.DataFrame:
        """
        分析所有公司对的关联关系
        
        Args:
            df: 输入数据
            column_a: A列列名
            column_b: B列列名
            
        Returns:
            包含分析结果的DataFrame
        """
        self.results = []
        
        # 尝试自动识别列名
        if column_a not in df.columns:
            # 尝试第一列
            column_a = df.columns[0]
            print(f"使用第一列作为公司A列: {column_a}")
        
        if column_b not in df.columns:
            # 尝试第二列
            if len(df.columns) > 1:
                column_b = df.columns[1]
            else:
                raise ValueError("数据至少需要包含两列")
            print(f"使用第二列作为公司B列: {column_b}")
        
        print(f"\n开始分析 {len(df)} 对公司关系...")
        print("=" * 60)
        
        for idx, row in df.iterrows():
            company_a = str(row[column_a]).strip()
            company_b = str(row[column_b]).strip()
            
            # 跳过空值
            if pd.isna(row[column_a]) or pd.isna(row[column_b]) or \
               company_a == 'nan' or company_b == 'nan' or \
               not company_a or not company_b:
                print(f"第 {idx + 1} 行: 跳过（存在空值）")
                continue
            
            print(f"\n第 {idx + 1} 行: 查询 '{company_a}' 和 '{company_b}' 的关系...")
            
            try:
                result = self.query_relationship(company_a, company_b)
                self.results.append(result)
                
                # 显示关联关系
                relationships = result['关联关系']
                if relationships:
                    for rel in relationships:
                        print(f"  └─ {rel}")
                else:
                    print(f"  └─ 未找到关联关系")
                    
            except Exception as e:
                print(f"  └─ 查询失败: {str(e)}")
                self.results.append({
                    '公司A': company_a,
                    '公司B': company_b,
                    '关联关系': [f'查询失败: {str(e)}'],
                    '查询时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    '查询状态': '失败'
                })
        
        print("\n" + "=" * 60)
        print(f"分析完成！共处理 {len(self.results)} 对公司关系")
        
        # 转换为DataFrame
        results_df = pd.DataFrame(self.results)
        
        # 将关联关系列表转换为字符串
        results_df['关联关系'] = results_df['关联关系'].apply(
            lambda x: '; '.join(x) if isinstance(x, list) else str(x)
        )
        
        return results_df
    
    def save_results(self, results_df: pd.DataFrame, output_path: str):
        """
        保存结果到文件
        
        Args:
            results_df: 结果DataFrame
            output_path: 输出文件路径
        """
        file_ext = os.path.splitext(output_path)[1].lower()
        
        try:
            if file_ext in ['.xlsx', '.xls']:
                results_df.to_excel(output_path, index=False, engine='openpyxl')
            elif file_ext == '.csv':
                results_df.to_csv(output_path, index=False, encoding='utf-8-sig')
            else:
                raise ValueError(f"不支持的输出格式: {file_ext}")
            
            print(f"\n结果已保存到: {output_path}")
        except Exception as e:
            raise Exception(f"保存结果失败: {str(e)}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='公司关联关系查询程序',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python company_relationship_analyzer.py input.xlsx -o output.xlsx
  python company_relationship_analyzer.py input.csv -o output.csv --api-key YOUR_API_KEY
  python company_relationship_analyzer.py input.xlsx -o output.xlsx -a 公司名称 -b 关联公司
        """
    )
    
    parser.add_argument('input_file', help='输入文件路径（Excel或CSV）')
    parser.add_argument('-o', '--output', default='company_relationships_result.xlsx',
                        help='输出文件路径（默认: company_relationships_result.xlsx）')
    parser.add_argument('-a', '--column-a', default='A列',
                        help='公司A列的列名（默认: 自动识别第一列）')
    parser.add_argument('-b', '--column-b', default='B列',
                        help='公司B列的列名（默认: 自动识别第二列）')
    parser.add_argument('--api-key', help='API密钥（如使用第三方API）')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"错误: 输入文件不存在: {args.input_file}")
        return
    
    print("=" * 60)
    print("公司关联关系查询程序")
    print("=" * 60)
    
    # 创建分析器
    analyzer = CompanyRelationshipAnalyzer(api_key=args.api_key)
    
    try:
        # 读取输入文件
        df = analyzer.read_input_file(args.input_file)
        
        # 分析关联关系
        results_df = analyzer.analyze_all(df, args.column_a, args.column_b)
        
        # 保存结果
        analyzer.save_results(results_df, args.output)
        
        print("\n程序执行完成！")
        
    except Exception as e:
        print(f"\n错误: {str(e)}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
