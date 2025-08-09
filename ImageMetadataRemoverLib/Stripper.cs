using MetadataExtractor;
using System.Drawing;

namespace ImageMetadataRemoverLib
{
    public class Stripper
    {
        public bool TryStrip(Stream stream)
        {
            var metaList = ImageMetadataReader.ReadMetadata(stream);

            foreach(var meta in metaList)
            {
                foreach(var tag in meta.Tags)
                {
                    if (tag.Name == "Description")
                        return true;
                }
            }

            return false;
        }
    }
}
