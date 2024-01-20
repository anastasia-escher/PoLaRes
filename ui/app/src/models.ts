export interface Author {
  author_id: string
  birth_date: string
  death_date: string
  description: string
  first_name: string
  last_name: string
  patronym: string
}

export type TextItem = {
  token: string
  lemma: string
  pos: string
  morphosyntactic_features: string
  line_number: string
}

export type Poem = {
  title: string
  text: TextItem[]
}

type CorpusAuthor = {
  [poemId: string]: Poem
}

export type Root = {
  [authorId: string]: CorpusAuthor
}

export interface Author {
  author_id: string
  birth_date: string
  death_date: string
  description: string
  first_name: string
  last_name: string
  patronym: string
}

export type PoemByLines = {
  [lineNumber: string]: TextItem[]
}

export type MetadataItem = {
  text_id: string
  date: number
  author_id: string
  metre: string
  genres: string
  associated_person: string
  associated_person_url: string
  text_source: string
  text_source_url: string
}
