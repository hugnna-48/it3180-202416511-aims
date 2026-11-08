def search_by_title(items, keyword):
    """
    Tìm kiếm đĩa trong danh sách dựa trên tiêu đề.
    
    Args:
        items: Danh sách các đĩa cần tìm kiếm.
        keyword: Từ khóa tìm kiếm.
        
    Returns:
        Danh sách các đĩa có tiêu đề khớp với từ khóa (không phân biệt hoa thường).
    """
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
