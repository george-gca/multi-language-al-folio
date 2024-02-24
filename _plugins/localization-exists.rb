module Jekyll
  class LocalizationExistsTag < Liquid::Tag
    def initialize(tag_name, key, tokens)
      super
      @key = key.strip()
    end

    def render(context)
      content = Liquid::Template.parse(@key).render context
      exists = true
      language = context.registers[:site].config['languages'].first
      if !content.include? "." or context.registers[:site].data[language] == nil
        exists = false
      end

      current_element = context.registers[:site].data[language]['strings']
      splittedKey = content.split('.')

      if exists
        for part in splittedKey do
          if current_element.key?(part)
            current_element = current_element[part]
          else
            exists = false
            break
          end
        end
      end

      "#{exists}"
    end
  end
end

Liquid::Template.register_tag('localization_exists', Jekyll::LocalizationExistsTag)
