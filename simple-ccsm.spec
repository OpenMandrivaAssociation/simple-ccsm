%define name simple-ccsm
%define version 0.7.8
%define rel 1
%define git 20080912

%if  %{git}
%define srcname %{name}-%{git}
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: Simple Compiz Config Settings Manager
Group: System/X11
URL: http://www.compiz-fusion.org/
Source: %{srcname}.tar.bz2
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: compiz-devel
BuildRequires: compizconfig-python-devel
BuildRequires: pygtk2.0-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Requires: compizconfig-python
Requires: pygtk2.0
Suggests: python-sexy

%description
Simple Compiz Config Settings Manager

%prep
%setup -q -n %{distname}

%build
python setup.py build --prefix=%{_prefix}

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -f %{buildroot}%{py_puresitedir}/*.egg-info
%find_lang %{name}


desktop-file-install \
  --vendor="" \
  --remove-category="Compiz" \
  --add-category="GTK" \
  --add-category="Settings" \
  --add-category="DesktopSettings" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.png
%{_datadir}/%{name}/images/*.svg
%dir %{_datadir}/%{name}/profiles
%{_datadir}/%{name}/profiles/*.profile
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
