<script setup lang="ts">
import CenteredContainer from 'layouts/CenteredContainer.vue'

const projectParticipants = [
  {
    name: 'Peter Sjökvist',
    affiliation: 'Uppsala University',
    href: 'https://www.katalog.uu.se/profile/?id=N3-457',
    description:
      'Peter Sjökvist is associate professor of Latin at Uppsala University and librarian in the Special Collections Division at Uppsala University Library. ' +
      'He is the project manager PoLaReS, particularly responsible for external relations.',
  },
  {
    name: 'Arsenii Vetushko-Kalevich',
    affiliation: 'Lund University',
    href: 'https://www.lunduniversity.lu.se/lucat/user/431826ffb8fd06c6f745f3165b971934',
    description:
      'Arsenii Vetushko-Kalevich is a researcher in Latin at Lund University. ' +
      'In the PoLaReS project, his particular area of responsibility is the contents of the database.',
  },
  {
    name: 'Anastasia Escher',
    affiliation: 'Swiss Federal Institute of Technology',
    href: 'https://www.nexus.ethz.ch/about/people1/person-detail.html?persid=305327',
    description:
      'Anastasia Escher is a software engineer at the Swiss Federal Institute of Technology. ' +
      'In the PoLaReS project, she is responsible for the development of the web application and other technical issues.',
  },
]
</script>

<template>
  <CenteredContainer max-width="1000px" title="About the project" title_class="tw-text-green-500">
    <div class="md:tw-tw-max-w-2xl tw-tw-mx-auto cont">
      <p class="tw-mb-4 tw-text-xl tw-font-semibold tw-text-coolGray-800"> Project Participants </p>
      <div class="tw-text-base md:tw-text-lg tw-text-coolGray-500">
        <ul>
          <li class="q-mt-md" v-for="participant in projectParticipants" :key="participant.name">
            <a target="_blank" class="cursor-pointer text-blue-8" :href="participant.href">{{
              participant.name
            }}</a>
            <br />
            <span class="text-grey-7 tw-text-sm">{{ participant.affiliation }}</span>
            <br />
            <p>{{ participant.description }}</p>
          </li>
        </ul>
      </div>
      <!--      <q-list class="tw-text-base md:tw-text-lg tw-text-coolGray-500">-->
      <!--        <q-item v-for="participant in projectParticipants" :key="participant.name">-->
      <!--          <q-item-section>-->
      <!--            <q-item-label-->
      <!--              ><a target="_blank" class="cursor-pointer text-blue-8" :href="participant.href">{{-->
      <!--                participant.name-->
      <!--              }}</a></q-item-label-->
      <!--            >-->
      <!--            <q-item-label caption>{{ participant.affiliation }}</q-item-label>-->
      <!--            <q-item-label>{{ participant.description }}</q-item-label>-->
      <!--          </q-item-section>-->
      <!--        </q-item>-->
      <!--      </q-list>-->

      <p class="tw-mb-4 tw-mt-4 tw-text-xl tw-font-semibold tw-text-coolGray-800"> Useful Links </p>

      <div class="tw-text-base md:tw-text-lg tw-text-coolGray-500"
        >Check out useful resources
        <a class="cursor-pointer text-blue-8" href="https://ianls.com/resources-2/" target="_blank">here</a
        >.</div
      >
    </div>
  </CenteredContainer>
</template>

<style scoped lang="scss"></style>
