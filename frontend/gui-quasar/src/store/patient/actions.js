export function setCurrentPatient (context, {patient}) {
    context.commit('setCurrentPatient', {patient: patient})
}
