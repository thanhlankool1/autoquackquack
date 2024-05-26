# autoquackquack
Xin chào các bạn hôm nay mình sẽ hướng dẫn các bạn viết auto nhặt trứng và ấp trứng của con AirDrop đang hot hiện tại quackquack free 100%

Mình sẽ tìm thêm cách auto các air khác và hướng dẫn các bạn trong thời gian sớm nhất.......

<!-- các bước thực hiện -->
đầu tiên F12 trình duyệt web lên mình lấy đc 1 vài API để sử dụng cho tool
này sẽ dựa vào kinh nghiệm để biết API nào có thể sài được nhé
đi phân tích từng API cùng mình nhé
sau khi mình xem thì mình đưa ra đc 1 API này

Step 1 : tìm hiểu các API cần sử dụng trên game quack quack sau khi ngồi xem cách request của game. mình lấy ra đc các api sau
    - API get danh sach trứng và vịt đang có trên map:
        https://api.quackquack.games/nest/list-reload
         - field cần quan tâm nest (trứng trong ổ): nest[id], nest[status]
         - field cần quan tâm duck: duck[id], duck[total_rare]
    - API lấy trứng:
        https://api.quackquack.games/nest/collect
    - API ấp trứng:
        https://api.quackquack.games/nest/hatch
    - API mở trứng:
        https://api.quackquack.games/nest/collect-duck
Step 2: setup môi trường
    - Tạo môi trường ảo
        + python3.12 -m venv venv-quackquack
    - Truy cập môi trường ảo (macos):
        + source venv-quackquack/bin/activate
    - Install các thư viện cần thiết 
        + python -m pip install -r requirements.txt
Step 3: code thôi: mình sẽ làm cấu trúc source tương tự các dự án thật tế:
    + thư mục utils để chứa các tính năng sử dụng lại nhiều lần như logger, request, connect db, bla bla ...
    + file quác quác để chạy nhé: này mình đã có code trước nên sẽ copy cho video ngắn nhất. và mình sẽ để source code phía dưới cho các bạn cần


doạn code httpx đó mình tận dụng lại source cũ. nó sẽ hỗ trợ trả lỗi khi gặp luôn. giúp code các bạn k bị lỗi ngoại lệ