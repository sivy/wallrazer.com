module Wallrazer
  class RandNum < Liquid::Tag

    def initialize(tag_name, max, tokens)
      super
      @max = max
    end

    def render(context)
      rand(@max.to_i)
    end
  end
end

Liquid::Template.register_tag('rand', Wallrazer::RandNum)