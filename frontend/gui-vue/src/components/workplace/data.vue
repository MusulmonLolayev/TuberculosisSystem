<template>
  <v-container fluid>
    <v-data-iterator
      :items="PATIENTS"
      :items-per-page.sync="itemsPerPage"
      :page="page"
      :search="search"
      :sort-by="sortBy.toLowerCase()"
      :sort-desc="sortDesc"
      hide-default-footer
      loading
      loading-text="Loading... Please wait"
    >
      <template v-slot:header>
        <v-toolbar
          dark
          color="blue darken-3"
          class="mb-1"
        >
          <v-text-field
            v-model="search"
            clearable
            flat
            solo-inverted
            hide-details
            label="Search"
          ></v-text-field>
          <template v-if="$vuetify.breakpoint.mdAndUp">
            <v-spacer></v-spacer>
            <v-select
              v-model="sortBy"
              flat
              solo-inverted
              hide-details
              :items="keys"
              label="Sort by"
              clearable
            >
            
            </v-select>
            <v-spacer></v-spacer>
            <v-btn-toggle
              v-model="sortDesc"
              mandatory
            >
              <v-btn
                large
                depressed
                color="blue"
                :value="false"
              >
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn
                large
                depressed
                color="blue"
                :value="true"
              >
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </template>
        </v-toolbar>
      </template>

      <template v-slot:default="props">
        <v-row>
          <v-col
            v-for="item in props.items"
            :key="item.name"
            cols="12"
            sm="5"
            md="3"
            lg="4"
          >
            <v-card>
              <v-card-title class="blue white--text">
                  <span>
                    {{ item.last_name + " " + item.first_name[0] + "." + item.middle_name[0] + "."}}
                  </span>
                  <v-spacer></v-spacer>
                  <v-menu bottom left>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        dark
                        icon
                        v-bind="attrs"
                        v-on="on"
                      >
                        <v-icon>mdi-dots-vertical</v-icon>
                      </v-btn>
                    </template>

                    <v-list>
                      <v-list-item
                        :key="1"
                        @click="mnudetails(item)"
                      >
                        <v-list-item-title>Details</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
              </v-card-title>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item :key="0">
                  <v-list-item-content :class="{ 'blue--text': sortBy === filteredKeys[0] }">
                    Number:
                  </v-list-item-content>
                  <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === filteredKeys[0] }">
                    {{item['number']}}
                  </v-list-item-content>
                </v-list-item>

                <v-list-item :key="1">
                  <v-list-item-content :class="{ 'blue--text': sortBy === filteredKeys[1] }">
                    Birthday:
                  </v-list-item-content>
                  <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === filteredKeys[1] }">
                    {{item['birthday']}}
                  </v-list-item-content>
                </v-list-item>

                <v-list-item :key="2">
                  <v-list-item-content :class="{ 'blue--text': sortBy === filteredKeys[2] }">
                    From date:
                  </v-list-item-content>
                  <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === filteredKeys[2] }">
                    {{item['fromdate']}}
                  </v-list-item-content>
                </v-list-item>

                <v-list-item :key="3">
                  <v-list-item-content :class="{ 'blue--text': sortBy === filteredKeys[3] }">
                    Gender:
                  </v-list-item-content>
                  <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === filteredKeys[3] }">
                    {{item['gender'] == true ? 'Male' : 'Female'}}
                  </v-list-item-content>
                </v-list-item>
                
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <template v-slot:footer>
        <v-row class="mt-2" align="center" justify="center">
          <span class="grey--text">Items per page</span>
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                dark
                text
                color="primary"
                class="ml-2"
                v-bind="attrs"
                v-on="on"
              >
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item
                v-for="(number, index) in itemsPerPageArray"
                :key="index"
                @click="updateItemsPerPage(number)"
              >
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span
            class="mr-4
            grey--text"
          >
            Page {{ page }} of {{ numberOfPages }}
          </span>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="mr-1"
            @click="formerPage"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="ml-1"
            @click="nextPage"
          >
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    data () {
      return {
        itemsPerPageArray: [4, 8, 12, 16],
        search: '',
        filter: {},
        sortDesc: false,
        page: 1,
        itemsPerPage: 8,
        sortBy: 'name',
        keys: [
          'number',
          'birthday',
          'fromdate',
          'gender'
        ],
      }
    },
    computed: {
      numberOfPages () {
        return Math.ceil(this.PATIENTS.length / this.itemsPerPage)
      },
      filteredKeys () {
        return this.keys.filter(key => key !== `Name`)
      },
      ...mapGetters([
            'PATIENTS'
        ]),
    },
    methods: {
      nextPage () {
        if (this.page + 1 <= this.numberOfPages) this.page += 1
      },
      formerPage () {
        if (this.page - 1 >= 1) this.page -= 1
      },
      updateItemsPerPage (number) {
        this.itemsPerPage = number
      },
      ...mapActions([
            'GET_PATIETNS_FROM_API'
        ]),
      mnudetails(patient){
        this.$router.push(
          {
            name: 'detials', 
            params: {patient: patient}
          })
      }
    },
    mounted(){
      this.GET_PATIETNS_FROM_API()
    }
  }
</script>