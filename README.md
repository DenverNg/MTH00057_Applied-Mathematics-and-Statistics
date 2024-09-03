# MTH00057_Applied-Mathematics-and-Statistics

### Project 01: 9.5đ 
`E1(-0.5): khởi tạo centroids "random" không kiểm tra centroids bị lặp. E2(-0): Báo cảo viết tốt, nên thay "Cộng tác viên" => công cụ hỗ trợ hoặc acknowledgement,...`

**Solution:**
```python
if init_centroids == 'random':
        centroids = np.zeros((k_clusters,img_1d.shape[1]))
        for i in range(k_clusters):
          while True:
            centroid = np.random.randint(0, 256, size = img_1d.shape[1])
            if not np.any(np.all(centroids == centroid, axis = 1)):
                centroids[i] = centroid
                break
        return centroids
```

### Project 02: 10đ
` 	E1(-0.5):Lưu tên ảnh sai quy định (Tên ảnh lưu sai quy đình (_.) B(+0.5):Có zoom in zoom out đúng` 

**Có thể lỗi ở phần đặt tên `zoom0.5x`**

**Note:** Phần in kết quả dưới dạng bảng phải làm giống template của thầy. Nếu không giống thì -0.5 (đừng hỏi vì sao mình không làm mà không bị trừ tại mình cũng không biết)

### Project 03: 10đ
`code + báo cáo ok`

### Nếu bạn sử dụng code của repo này trong đồ án, vui lòng trích nguồn đầy đủ