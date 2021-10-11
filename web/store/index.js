const actions = {
  onAuthStateChangedAction(state, { authUser, claims }) {
    if (!authUser) {
      state.commit('SET_USER', null)
      this.$router.push({
        path: '/login',
      })
    } else {
      const { uid } = authUser
      state.commit('SET_USER', uid)
    }
  },
}

const mutations = {
  SET_USER(state, uid) {
    state.uid = uid
  },
}

const state = () => ({
  uid: null,
})

const getters = {
  getUid(state) {
    return state.uid
  },
}

export default {
  state,
  actions,
  mutations,
  getters,
}
