# spotify api와 music brainz api
- spotify api로 많은 양의 노래 데이터를 불러올 수 있지만 노래의 장르가 데이터에 없음
- spotify api는 장르를 노래가 아닌 가수에 부여함 -> 각 노래의 장르가 아니라 가수의 장르가 되어버린다.
- music brainz api는 사용자들의 참여를 통해 데이터가 만들어지지만 정보의 정확성이 높음
- music brainz api는 tag라는 이름을 통해 노래의 장르를 파악할 수 있지만 노래 1개씩밖에 검색이 안됨
- 따라서 이 두개의 api를 적절히 활용하여 spotify로 노래 검색 -> music brainz에서 해당 노래의 Id 검색 -> Id를 통해 해당 노래의 장르 검색하는 과정을 거친다.
- 이 과정에서 tag가 작성되지 않은 경우, 'Undefined'로 정의한다 -> 추후 홈페이지 사용자가 직접 추가할 수 있게
- tag가 여러 개 있을 수 있기 때문에 한 노래당 tag를 최대 3개 할당한다.