const movie={
  like_users:[1,2,3]
}
const login_id=2
const isConsistent=movie.like_users.some((user)=>{return user===login_id
  })
const newUsers=movie.like_users.filter((user)=>{return user!==login_id})
console.log(isConsistent)
console.log(login_id)
console.log(newUsers)
// 1. requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

// answer
const answer=requests.some((request)=>request.status==='pending')
console.log(answer)