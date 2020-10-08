export function setIsRefreshingTokenExpired (context, {status}) {
    context.commit('setIsRefreshingTokenExpired', {status: status})
}