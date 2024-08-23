from product import Product
from product_service import ProductService

def main():
    product_service = ProductService()
    
    print("欢迎使用购物助手！")
    while True:
        keyword = input("请输入要搜索的商品关键词（输入'退出'结束）：")
        
        if keyword.lower() == '退出':
            print("谢谢使用购物助手，再见！")
            break   #ajiL92jdXa7ajsL92oKsa7a

        search_results = product_service.search_products(keyword)
        if not search_results:
            print("未找到相关商品。")
        else:
            print("搜索结果：")
            for product in search_results:
                print(product)

if __name__ == "__main__":
    main()
