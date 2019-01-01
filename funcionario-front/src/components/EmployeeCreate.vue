<template>
    <v-form style="background-color:#fff;" ref="form" >

        <v-toolbar dark color="blue darken-1" @click="$router.push('/movimento-list')" style="cursor: pointer">
            <v-icon small >arrow_back</v-icon>
            <v-toolbar-title class="subheading">
                Voltar
            </v-toolbar-title>
        </v-toolbar>
        <v-container>
            <v-layout row wrap>
                <v-flex xs12 sm4>
                    <v-select
                      :items="AllRegios"
                      label="Região Hidrográfica"
                      item-text="name"
                      item-value="id"
                      v-model="region"
                      id="region"
                      @change="setRegion(region)"
                    >
                    </v-select>
                </v-flex>
                <v-flex xs11 sm4>
                    <v-menu
                      ref="menuDate"
                      :close-on-content-click="false"
                      v-model="menuDate"
                      :nudge-right="40"
                      :return-value.sync="date"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      max-width="290px"
                      min-width="290px"
                    >
                        <v-text-field
                          slot="activator"
                          v-model="date"
                          label="Data do Movimento"
                          prepend-icon="event"
                          readonly
                          :mask="'####/##'"
                          id="date"

                        ></v-text-field>
                        <v-date-picker
                          v-model="date"
                          type="month"
                          no-title
                          scrollable
                          locale="pt"
                        >
                            <v-spacer></v-spacer>
                            <v-btn flat color="primary" @click="menuDate = false">Cancelar</v-btn>
                            <v-btn flat color="primary" @click="handler($refs, date)">OK</v-btn>
                        </v-date-picker>
                    </v-menu>
                </v-flex>
            </v-layout>
            <v-layout  wrap v-for="(data,index) in AllMoves" :key="index">
                    <v-flex xs12 sm6>
                        <v-text-field
                                label="Origem"
                                v-model="AllMoves[index].name"
                                id="AllMoves"
                                item-value="value"
                                disabled
                        ></v-text-field>
                    </v-flex>
                    <input type="hidden" v-model="AllMoves[index].moveId" class="moves">
                    <v-flex xs12 sm6>
                        <v-text-field
                                label="Valor"
                                v-model="valueMovements[index]"
                                :ref="'valor'+index"
                        ></v-text-field>
                    </v-flex>
            </v-layout>

            <div style="text-align: right">
                <v-btn small color="success" @click="CreateOrUpdate">Salvar</v-btn>
            </div>
        </v-container>
    </v-form>
</template>


<script>
  function makeUrl (id) {
    return 'movimento/' + id + '/'
  }
  export default {
    data: () => ({
      AllMoves: [],
      AllRegios: [],
      originMovements: [],
      valueMovements: [],
      idMovements: [],
      CreateOrUpdateItem: {
        origim_movement: '',
        value: 0
      },
      date: null,
      year: null,
      month: null,
      region: '',
      formOrigins: [],
      menuDate: false
    }),
    created () {
      this.initialize()
    },
    methods: {
      initialize () {
        this.axios.get('/regiao/')
          .then(response => {
            this.AllRegios = response.data['results']
          })
          .catch(error => {
            console.log(error)
          })
      },

      handler (refs, date) {
        refs.menuDate.save(date)
        this.getAllMoves()
      },

      getAllMoves () {
        this.year = this.date.toString().substring(0, 4)
        this.month = this.date.toString().substr(-1)

        console.log(this.month)

        this.axios.get(`/movimento/existencia/?year=${this.year}&month=${this.month}&rh=${this.region}`)
        .then(response => {
          this.AllMoves = response.data
          this.valueMovements = []
          response.data.map((item, i) => {
            this.valueMovements.push(item.value)
            this.originMovements.push(item.id)
            if (item.moveId !== undefined) this.idMovements.push(item.moveId)
          })
        })
        .catch(error => {
          console.log(error)
        })
      },

      setRegion (region) {
        self.region = region
      },
      CreateOrUpdate (moveId = null, value) {
        if (this.idMovements.length > 0) {
          for (let i = 0; i < this.idMovements.length; i++) {
            axiosAuth.put(makeUrl(this.idMovements[i]), {
              value: this.valueMovements[i],
              month: this.month,
              year: this.year,
              origin_movement: `http://127.0.0.1:8000/api/origem/${this.originMovements[i]}/`,
              rh: `http://127.0.0.1:8000/api/regiao/${this.region}/`
            })
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              console.log(error)
              this.$toast.error('Erro ao criar registros!', 'Ops', {position: 'bottomRight'})
            })
          }
          this.$toast.success('Registros inseridos com sucesso!!', 'OK', {position: 'bottomRight'})
        } else {
          for (let i = 0; i < this.valueMovements.length; i++) {
            axiosAuth.post('movimento/', {
              value: this.valueMovements[i],
              month: this.month,
              year: this.year,
              origin_movement: `http://127.0.0.1:8000/api/origem/${this.originMovements[i]}/`,
              rh: `http://127.0.0.1:8000/api/regiao/${this.region}/`
            })
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              console.log(error)
              this.$toast.error('Erro ao atualizadar registros!', 'Ops', {position: 'bottomRight'})
            })
          }
          this.$toast.success('Registros atualizados com sucesso!', 'OK', {position: 'bottomRight'})
        }
      }

    }
  }
</script>