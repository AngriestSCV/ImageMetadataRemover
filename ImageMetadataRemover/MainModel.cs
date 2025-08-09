using ImageMetadataRemoverLib;
using Prism.Commands;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace ImageMetadataRemover
{
    public class MainModel: BindableBase
    {
        private string _selectedPath = @"C:\src\ImageMetadataRemover\with-metadata.png";
        private readonly Stripper _stripper;

        public ICommand Strip { get; }
        public string SelectedPath
        {
            get => _selectedPath;
            set => SetProperty(ref _selectedPath, value);
        }

        public MainModel(Stripper stripper)
        {
            _stripper = stripper;
            Strip = new DelegateCommand(DoStrip);
        }

        private void DoStrip()
        {
            using (var file = File.Open(_selectedPath, FileMode.Open)) {
                _stripper.TryStrip(file);
            }
        }
    }
}
