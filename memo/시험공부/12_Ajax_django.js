// Ajax(Asynchronous JavaScript and XML, 에이잭스)는 비동기적인 웹 애플리케이션의 제작을 위해
// 아래와 같은 조합을 이용하는 웹 개발 기법이다.

/*

* 조합
- 표현 정보를 위한 HTML / CSS
- 동적인 화면 출력 및 표시 정보와의 상호작용을 위한 DOM, JS
- 웹 서버와 비동기적으로 데이터를 교환하고 조작하기 위한 데이터 - JSON(XML)
* Ajax 애플리케이션은 필요한 데이터만을 웹서버에 요청해서 받은 후 클라이언트에서
  데이터에 대한 처리를 할 수 있다.
* 이것은 이미 존재하던 기술이었지만 2000년도 중반 이후로 인기를 끌기 시작했다.
  구글은 2004년에 G메일, 2005년에 구글 지도 등의 웹 애플리케이션을 만들기 위해
  비동기식 통신을 사용했다.
* 웹 서버의 응답을 처리하기 위해 클라이언트 쪽에서는 자바스크립트를 쓴다.
  웹 서버에서 전적으로 처리되던 데이터 처리의 일부분이 클라이언트 쪽에서 처리되므로 
  웹 브라우저와 웹 서버 사이에 교환되는 데이터량과 웹서버의 데이터 처리량도 줄어들기 때문에
  애플리케이션의 응답성이 좋아진다.
* 한편, 웹 개발자들은 때때로 Ajax를 단순히 웹 페이지의 일부분을 대체하기 위해 사용한다.
  비 AJAX 사용자가 전체 페이지를 불러오는 것에 비해 Ajax 사용자는 페이지의 일부분만을 불러올 수가 있다.
  이것으로 개발자들이 비 AJAX 환경에 있는 사용자의 접근성을 포함한 경험을 보호할 수 있으며,
  적절한 브라우저를 이용하는 경우에 전체 페이지를 불러오는 일 없이 응답성을 향상시킬 수 있다.

*/