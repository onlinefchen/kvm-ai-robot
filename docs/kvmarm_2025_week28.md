# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:05:38

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 226
- **总 Thread 数**: 30
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 21 threads (201 邮件)
- **RFC**: 1 threads (1 邮件)
- **Bug Report**: 1 threads (1 邮件)
- **GIT PULL**: 3 threads (7 邮件)
- **Other**: 4 threads (16 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 37 | **👥 参与者**: 6 | **📅 开始时间**: Wed,  9 Jul 2025 11:59:26 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）中支持用户空间映射的补丁系列，主要针对使用 `guest_memfd` 作为内存后端的非 CoCo 虚拟机。该补丁系列的核心内容是实现用户空间对 `guest_memfd` 支持的内存的映射，旨在增强 KVM 的内存管理能力和安全性。

**补丁内容**：
补丁系列的主要目标是允许 KVM 在非 CoCo 虚拟机中实现对 `guest_memfd` 支持的内存的映射，具体包括：
1. 重新命名和扩展 Kconfig 选项，以更好地反映功能。
2. 引入新的能力标志 `KVM_CAP_GMEM_MMAP`，用于指示用户空间是否支持 `guest_memfd` 的映射。
3. 实现对 `guest_memfd` 的 mmap 支持，包括对 x86 和 arm64 架构的支持。

**历史讨论要点**：
在之前的讨论中，参与者强调了对 `guest_memfd` 的支持如何简化虚拟机管理器（VMM）的设计，并提高安全性，特别是在防范类似 Spectre 的攻击方面。补丁的设计旨在使 `guest_memfd` 能够支持更广泛的用例，包括共享内存的场景。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现和潜在的错误修复上。参与者对补丁进行了审查，提出了对代码的改进建议，并讨论了如何处理与内存无效化相关的竞争条件。此外，针对 arm64 架构的补丁也得到了审查，确保其在处理 `guest_memfd` 时的正确性。

总的来说，这个补丁系列通过引入对 `guest_memfd` 的支持，增强了 KVM 的灵活性和安全性，得到了社区的积极反馈和审查。

#### 📝 邮件列表

1. **[07-09 11:59]** [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-09 11:59]** [PATCH v13 01/20] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-09 11:59]** [PATCH v13 02/20] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-09 11:59]** [PATCH v13 03/20] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-09 11:59]** [PATCH v13 04/20] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-09 11:59]** [PATCH v13 05/20] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-09 11:59]** [PATCH v13 06/20] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-09 11:59]** [PATCH v13 07/20] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-09 11:59]** [PATCH v13 08/20] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-09 11:59]** [PATCH v13 09/20] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-09 11:59]** [PATCH v13 10/20] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-09 11:59]** [PATCH v13 11/20] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-09 11:59]** [PATCH v13 12/20] KVM: x86/mmu: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-09 11:59]** [PATCH v13 13/20] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[07-09 11:59]** [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default VM type
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[07-09 11:59]** [PATCH v13 15/20] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[07-09 11:59]** [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-09 11:59]** [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[07-09 11:59]** [PATCH v13 18/20] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[07-09 11:59]** [PATCH v13 19/20] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[07-09 11:59]** [PATCH v13 20/20] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[07-11 09:14]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: kernel test robot <lkp@intel.com>
23. **[07-11 14:04]** Re: [PATCH v13 09/20] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Shivank Garg <shivankg@amd.com>
24. **[07-11 14:18]** Re: [PATCH v13 18/20] KVM: Introduce the KVM capability
 KVM_CAP_GMEM_MMAP
   - 发件人: Shivank Garg <shivankg@amd.com>
25. **[07-11 11:36]** Re: [PATCH v13 10/20] KVM: x86/mmu: Generalize
 private_max_mapping_level x86 op to max_mapping_level
   - 发件人: David Hildenbrand <david@redhat.com>
26. **[07-11 11:38]** Re: [PATCH v13 11/20] KVM: x86/mmu: Allow NULL-able fault in
 kvm_max_private_mapping_level
   - 发件人: David Hildenbrand <david@redhat.com>
27. **[07-11 11:45]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: David Hildenbrand <david@redhat.com>
28. **[07-11 09:59]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
29. **[07-11 12:08]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
30. **[07-11 12:09]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Fuad Tabba <tabba@google.com>
31. **[07-11 14:25]** Re: [PATCH v13 15/20] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[07-11 14:49]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[07-11 15:17]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[07-11 15:25]** Re: [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared guest_memfd memory
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[07-11 15:34]** Re: [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
36. **[07-11 16:48]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[07-11 17:37]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 30 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  8 Jul 2025 10:25:05 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的多个补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复上。

1. **原始补丁内容**：补丁系列（[PATCH v3 00/27]）旨在修复 KVM 在处理 SCTLR2、DoubleFault2 以及 NV 外部中止时的多个问题，确保在虚拟化环境中能正确处理异常和中止。

2. **之前讨论要点**：在历史讨论中，参与者关注了如何正确处理 SError（系统错误）和外部中止的路由，尤其是在不同的上下文（如嵌套虚拟机）中。补丁中引入了对 SCTLR2 和 DoubleFault2 特性的检测，以便在虚拟机中正确配置和使用这些特性。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现和测试上，包括：
   - 增加对 SCTLR2_EL1 的支持和描述。
   - 确保在 HCRX_EL2.TMEA 设置时，"屏蔽"的外部中止能正确路由到 EL2。
   - 引入对 SError 的处理逻辑，确保在特定条件下（如 NMEA 设置）能正确响应 SError。
   - 增加自测用例，以验证 SError 注入和 SEA（同步外部中止）的处理是否符合预期。

最终，Oliver Upton 表示已将这些补丁应用到下一个版本中，感谢参与者的贡献。

#### 📝 邮件列表

1. **[07-08 10:25]** [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-08 10:25]** [PATCH v3 01/27] arm64: Detect FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-08 10:25]** [PATCH v3 02/27] arm64: Detect FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-08 10:25]** [PATCH v3 03/27] KVM: arm64: Add helper to identify a nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-08 10:25]** [PATCH v3 04/27] KVM: arm64: Treat vCPU with pending SError as runnable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-08 10:25]** [PATCH v3 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-08 10:25]** [PATCH v3 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-08 10:25]** [PATCH v3 07/27] KVM: arm64: nv: Add FEAT_RAS vSError sys regs to table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-08 10:25]** [PATCH v3 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[07-08 10:25]** [PATCH v3 09/27] KVM: arm64: nv: Advertise support for FEAT_RAS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[07-08 10:25]** [PATCH v3 10/27] KVM: arm64: nv: Describe trap behavior of SCTLR2_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[07-08 10:25]** [PATCH v3 11/27] KVM: arm64: Wire up SCTLR2_ELx sysreg descriptors
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[07-08 10:25]** [PATCH v3 12/27] KVM: arm64: Context switch SCTLR2_ELx when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[07-08 10:25]** [PATCH v3 13/27] KVM: arm64: Enable SCTLR2 when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[07-08 10:25]** [PATCH v3 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[07-08 10:25]** [PATCH v3 15/27] KVM: arm64: Factor out helper for selecting exception target EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[07-08 10:25]** [PATCH v3 16/27] KVM: arm64: nv: Ensure Address size faults affect correct ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[07-08 10:25]** [PATCH v3 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[07-08 10:25]** [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2 when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[07-08 10:25]** [PATCH v3 19/27] KVM: arm64: nv: Honor SError routing effects of SCTLR2_ELx.NMEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[07-08 10:25]** [PATCH v3 20/27] KVM: arm64: nv: Enable vSErrors when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[07-08 10:25]** [PATCH v3 21/27] KVM: arm64: Advertise support for FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[07-08 10:25]** [PATCH v3 22/27] KVM: arm64: Advertise support for FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[07-08 10:25]** [PATCH v3 23/27] KVM: arm64: Don't retire MMIO instruction w/ pending (emulated) SError
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
25. **[07-08 10:25]** [PATCH v3 24/27] KVM: arm64: selftests: Add basic SError injection test
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[07-08 10:25]** [PATCH v3 25/27] KVM: arm64: selftests: Test SEAs are taken to SError vector when EASE=1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[07-08 10:25]** [PATCH v3 26/27] KVM: arm64: selftests: Add SCTLR2_EL1 to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[07-08 10:25]** [PATCH v3 27/27] KVM: arm64: selftests: Catch up set_id_regs with the kernel
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[07-08 10:39]** Re: [PATCH v3 08/27] KVM: arm64: nv: Use guest hypervisor's vSError
 state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[07-08 12:00]** Re: [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 3: [PATCH v3 00/22] ARM64 PMU Partitioning

**📧 邮件数**: 17 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 26 Jun 2025 20:04:36 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 PMU（性能监控单元）分区的补丁系列，主要由 Colton Lewis 提出。该补丁旨在创建一种新的 PMU 方案，允许为虚拟机保留部分计数器，从而显著降低开销。补丁系列包括多个具体实现，如添加 HPMN0 功能、生成 sysreg 枚举的符号宏、清理 KVM 相关头文件等。

在历史讨论中，Colton 提出了多个补丁的初步版本，并讨论了实现细节和潜在问题。例如，补丁 v3 中提到将主机保留计数器的默认值设置为 -1，以避免与 0 的歧义，并对 KVM 和 PMU 之间的接口进行了重组。

在本周的新讨论中，参与者 Mark Rutland 和 Oliver Upton 对补丁进行了逐一审查，提出了一些建议和问题。Mark 对 HPMN0 的标记和枚举的处理表示认可，并提出了一些小的修改意见。同时，他也对 PMU 的分区配置提出了疑问，建议进一步明确分区的具体实现方式。Oliver 则关注补丁的命名问题，认为当前的“分区”可能会引起误解，建议使用更清晰的术语。

总体来看，本周的讨论集中在对补丁的细节审查和命名建议上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[06-26 20:04]** [PATCH v3 00/22] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-26 20:04]** [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-26 20:04]** [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-26 20:04]** [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-26 20:04]** [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-26 20:04]** [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[07-07 17:05]** Re: [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Mark Rutland <mark.rutland@arm.com>
8. **[07-07 17:07]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[07-07 17:13]** Re: [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Mark Rutland <mark.rutland@arm.com>
10. **[07-07 17:57]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Mark Rutland <mark.rutland@arm.com>
11. **[07-07 17:58]** Re: [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[07-07 12:07]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[07-08 22:34]** Re: [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[07-08 22:37]** Re: [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[07-08 22:38]** Re: [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[07-08 22:38]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[07-08 15:41]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 4: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 16 | **👥 参与者**: 6 | **📅 开始时间**: Sat, 5 Jul 2025 07:17:11 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM (Kernel-based Virtual Machine) 中将 GPU 设备内存映射为可缓存的补丁系列（PATCH v10 0/6）。该补丁旨在支持在 Grace Hopper 和 Blackwell 超级芯片等平台上，利用 CPU 可访问的缓存一致性 GPU 内存。补丁的主要内容包括：将设备内存映射为 NORMAL，以便支持缓存操作，重命名变量以更准确地反映其功能，更新检测设备内存的检查，以及允许基于 VMA 标志的可缓存映射。

在之前的讨论中，参与者们探讨了当前 KVM 对内存的强制映射限制，指出这可能导致安全隐患，尤其是在不同虚拟机之间共享内存时。补丁系列的设计旨在解决这些问题，确保内存属性的一致性。

本周的新进展包括，多个参与者（如 Catalin Marinas 和 David Hildenbrand）对补丁系列进行了审核并给予了“Reviewed-by”反馈。Ankit Agrawal 表达了对审核者的感谢，并确认 Oliver Upton 已将补丁应用到下一个开发树中。此外，Ankit 还提到对补丁进行了进一步的修改和完善，确保代码质量。整体来看，该补丁系列得到了积极的反馈，并已进入实施阶段。

#### 📝 邮件列表

1. **[07-05 07:17]** [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[07-05 07:17]** [PATCH v10 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[07-05 07:17]** [PATCH v10 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[07-05 07:17]** [PATCH v10 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[07-05 07:17]** [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
6. **[07-05 07:17]** [PATCH v10 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
7. **[07-06 19:51]** Re: [PATCH v10 1/6] KVM: arm64: Rename the device variable to
 s2_force_noncacheable
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
8. **[07-06 19:52]** Re: [PATCH v10 2/6] KVM: arm64: Update the check to detect device
 memory
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[07-06 19:54]** Re: [PATCH v10 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[07-06 20:00]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping
 using VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[07-06 20:02]** Re: [PATCH v10 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[07-07 09:32]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: David Hildenbrand <david@redhat.com>
13. **[07-07 09:27]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping
 using VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
14. **[07-07 16:39]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
15. **[07-07 16:57]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[07-09 14:34]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 5: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory

**📧 邮件数**: 11 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 24 Jun 2025 16:40:18 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中处理共享内存的 guest_memfd 的页面错误的补丁（PATCH v12 10/18）。该补丁旨在改进 KVM 对于使用共享内存的 guest_memfd 的支持，特别是在处理页面错误时的行为。

在历史讨论中，参与者探讨了如何在同一虚拟机中支持既可以 mmap 的 memslot 也可以不支持 mmap 的 memslot 的用例。Ackerley Tng 和其他参与者提出了不同的观点，讨论了命名的清晰性、用户空间对内存槽的控制以及在不同阶段支持 mmap 的策略。最终，大家达成一致，认为应先实现 mmap 功能，然后再处理更复杂的用例。

在本周的新讨论中，Sean Christopherson 和 Ackerley Tng 继续讨论了如何简化 KVM 的内部架构钩子，建议不支持在遗留 CoCo 虚拟机中使用 mmap。Sean 还提到可以使用 mseal() 来实现某些保护，而不必增加 KVM 的复杂性。Ackerley 表示将很快重新提交补丁，并感谢大家的澄清。

总体而言，讨论集中在如何有效地实现和管理 KVM 中的共享内存功能，确保在不同场景下的灵活性与简洁性。

#### 📝 邮件列表

1. **[06-24 16:40]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
2. **[06-27 08:01]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
3. **[06-30 09:07]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-30 07:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[06-30 16:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-01 00:56]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Shivank Garg <shivankg@amd.com>
7. **[06-30 22:03]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[07-01 07:15]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
9. **[07-01 16:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[07-07 17:05]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-08 06:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 6: [PATCH v2 02/15] KVM: selftests: Enable selftests runner to find
 executables in different path

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 9 Jul 2025 14:39:05 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测试（selftests）运行器的改进，主要集中在如何增强其功能以便更好地查找可执行文件和处理输出。

原始的 patch 提出了一个功能，允许自测试运行器在不同路径下查找可执行文件。参与者 Vipin Sharma 提出了这个改进，并在后续邮件中讨论了多个相关的 patch，包括添加超时选项、保存输出到目录、以及打印测试状态的标志等。

在之前的讨论中，参与者们对 patch 的命名和功能进行了深入探讨。Sean Christopherson 指出，使用 "executable" 这个术语可能会引起误解，建议使用更符合 Linux 习惯的 "-p/--path"。同时，关于输出的处理，Vipin 提出应避免使用过多的布尔选项，以简化用户的选择。

本周的新讨论中，主要集中在对命令行选项的反馈和改进建议上。Sean 对输出选项的复杂性表示担忧，并建议提供更清晰的 README 文档以帮助用户理解如何使用这些功能。此外，Oliver Upton 提出了对默认测试用例的处理方式的看法，认为应优先考虑减少噪音，只提交重要的测试配置，并考虑将生成测试用例的过程与构建分开，以避免不必要的文件覆盖。

总体来看，本周的讨论进一步推动了 KVM 自测试运行器的功能完善，参与者们积极提出建议和改进方案，以提升用户体验和代码的可维护性。

#### 📝 邮件列表

1. **[07-09 14:39]** Re: [PATCH v2 02/15] KVM: selftests: Enable selftests runner to find
 executables in different path
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-09 14:46]** Re: [PATCH v2 03/15] KVM: selftests: Add timeout option in selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-09 14:52]** Re: [PATCH v2 04/15] KVM: selftests: Add option to save selftest
 runner output to a directory
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-09 14:55]** Re: [PATCH v2 06/15] KVM: selftests: Add a flag to print only test
 status in KVM Selftests run
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-09 15:01]** Re: [PATCH v2 07/15] KVM: selftests: Add various print flags to KVM
 Selftest Runner
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-09 15:25]** Re: [PATCH v2 00/15] Add KVM Selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-09 15:25]** Re: [PATCH v2 03/15] KVM: selftests: Add timeout option in selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[07-09 16:06]** Re: [PATCH v2 11/15] KVM: selftests: Auto generate default tests for
 KVM Selftests Runner
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-09 17:18]** Re: [PATCH v2 11/15] KVM: selftests: Auto generate default tests for
 KVM Selftests Runner
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[07-09 17:20]** Re: [PATCH v2 01/15] KVM: selftest: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 7: [PATCH 0/2] Fix and add warning of misuse of type##_replace_bits()

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  3 Jul 2025 14:57:27 +0100

#### 🤖 AI 总结

本邮件讨论主要围绕两个补丁（patch）进行，旨在修复和增强对 `type##_replace_bits()` 函数的使用警告。

**原始补丁内容**：
第一个补丁（PATCH 0/2）由 Ben Horgan 提出，修复了 `u64_replace_bits()` 的使用错误，并在 `type##_replace_bits()` 函数中添加了 `__must_check` 注解，以确保返回值被检查。第二个补丁（PATCH 2/2）进一步强调了这一点，指出该函数没有副作用，因此只有在检查返回值的情况下才有用。

**之前讨论要点**：
在历史讨论中，Ben Horgan 提出了这两个补丁的必要性，并解释了添加 `__must_check` 的原因。参与者们对补丁的有效性表示支持，并讨论了如何确保代码的安全性和一致性。

**本周新讨论进展**：
本周的讨论中，Yury Norov 提出是否也应将 `_encode_bits()` 和 `_get_bits()` 标记为 `__must_check`，以统一使用标准。Ben Horgan 表示这可能不太重要，但愿意在后续版本中添加。Marc Zyngier 确认第一个补丁将通过 KVM/arm64 树合并，并表示支持 Yury 的后续补丁。Oliver Upton 提交了与 SError 相关的两个新补丁，并确认已将其应用到下一个版本中。

总体来看，讨论集中在确保代码安全性和一致性上，参与者们积极推动补丁的合并和进一步改进。

#### 📝 邮件列表

1. **[07-03 14:57]** [PATCH 0/2] Fix and add warning of misuse of type##_replace_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-03 14:57]** [PATCH 2/2] bitfield: Ensure the return value of type##_replace_bits() is checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[07-07 12:31]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Yury Norov <yury.norov@gmail.com>
4. **[07-08 10:42]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[07-08 10:45]** Re: [PATCH 2/2] bitfield: Ensure the return value of type##_replace_bits() is checked
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-08 10:46]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Yury Norov <yury.norov@gmail.com>
7. **[07-08 16:06]** [PATCH 0/2] KVM: arm64: Fix + test for SError ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-08 16:06]** [PATCH 1/2] KVM: arm64: Populate ESR_ELx.EC for emulated SError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-08 16:06]** [PATCH 2/2] KVM: arm64: selftests: Test ESR propagation for vSError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[07-09 09:59]** Re: [PATCH 0/2] KVM: arm64: Fix + test for SError ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 8: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 11 Jul 2025 12:39:50 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理同步外部中止（SEA）的补丁。补丁的主要目的是在 APEI（ACPI Platform Error Interface）无法处理 SEA 时，将事件重定向到用户空间，以便更优雅地处理可恢复的内存错误，避免虚拟机崩溃。

在历史讨论中，补丁提出了通过引入 `KVM_CAP_ARM_SEA_TO_USER` 功能，使用户空间能够处理 SEA 事件。补丁详细描述了如何在 KVM 中实现这一功能，包括新引入的退出原因 `KVM_EXIT_ARM_SEA`，并提供了关于 SEA 的详细信息，以便用户空间能够进行相应的处理。

在本周的新讨论中，参与者对补丁进行了审查和反馈。Oliver Upton 提出了避免在头文件中添加仅在单个调用点使用的辅助函数的建议，并讨论了如何处理与 FEAT_RAS（Reliability, Availability, and Serviceability）相关的情况。此外，Jiaqi Yan 和 Oliver Upton 讨论了如何在用户空间中提供更多的 ESR（Exception Syndrome Register）字段，以便更好地处理外部中止事件。

总体而言，本周讨论集中在补丁的细节修改和改进建议上，参与者们积极交流，推动补丁的进一步完善。

#### 📝 邮件列表

1. **[07-11 12:39]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-11 12:42]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-11 12:44]** Re: [PATCH v2 5/6] KVM: selftests: Test for KVM_CAP_INJECT_EXT_IABT
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-11 16:58]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[07-11 16:59]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
6. **[07-11 16:59]** Re: [PATCH v2 5/6] KVM: selftests: Test for KVM_CAP_INJECT_EXT_IABT
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
7. **[07-12 12:47]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-12 12:57]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-12 19:42]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 9: [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  9 Jul 2025 14:14:11 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁系列，主要涉及允许用户空间写入 GICD_TYPER2.nASSGIcap 的功能。

**原始补丁内容**：
补丁系列的核心是允许用户空间在初始化 VGIC（虚拟通用中断控制器）之前，修改 GICD_TYPER2.nASSGIcap 的值。这一修改旨在提高对虚拟处理单元（vPE）的管理能力，尤其是在资源受限的环境中。

**历史讨论要点**：
在之前的讨论中，开发者们探讨了如何处理 VGIC 的不同寄存器，尤其是 GICD_IIDR 的写入权限问题。讨论强调了在初始化之前允许对某些寄存器的写入，以便用户空间能够配置虚拟机的特性。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括对多个相关寄存器的访问权限调整。Oliver Upton 提出了最终的补丁版本，确保在 VGIC 初始化前，用户空间可以修改 GICD_TYPER2.nASSGIcap 和 GICD_IIDR。Raghavendra Rao Ananta 还增加了自测功能，以验证这些寄存器的可配置性。此外，文档也更新了用户空间对这些寄存器的访问预期。参与者们还就代码中的一些细节进行了讨论和修正，确保补丁的准确性和有效性。整体来看，这一系列补丁预计将在 6.17 版本中合并。

#### 📝 邮件列表

1. **[07-09 14:14]** [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-09 14:14]** [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-09 14:14]** [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-09 14:14]** [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-09 14:14]** [PATCH v4 4/6] KVM: arm64: vgic-v3: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-09 14:14]** [PATCH v4 5/6] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-09 14:14]** [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-10 09:59]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[07-10 09:22]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 20:41:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构中的 HIP10/HIP10C 错误（erratum 162200803）提出的补丁。该补丁旨在解决 GICv4.0 中的一个 SoC 缺陷，具体表现为在多个虚拟处理单元（vPE）同时发送调度命令时，可能会导致某些命令未被调度，从而引发超时问题。

在历史讨论中，参与者们探讨了该补丁的有效性和实现细节。Marc Zyngier 指出，当前的 KVM 实现并没有强制限制虚拟 LPI（vLPI）的数量，这可能导致问题的加剧。Zhou Wang 也承认需要在 MAPTI/MAPI 命令中增加对 LPI 数量的检查，以确保补丁的正确性。

在本周的新讨论中，Zhou Wang 提出了将 GICD_TYPE.num_LPIs 设置为可写字段的建议，并计划在虚拟机监控器（VMM）中进行配置，以便在不同的虚拟机之间迁移时能够正确处理 LPI 配置。Marc Zyngier 也表示支持这一思路，并认为将该错误处理逻辑纳入内核是更好的选择。Zhou Wang 最后确认将准备新的补丁以实现这一改进。

#### 📝 邮件列表

1. **[06-26 20:41]** [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[06-26 14:27]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-27 14:36]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[07-01 09:14]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-02 17:57]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[07-03 11:44]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-08 20:05]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
8. **[07-08 13:47]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-09 10:08]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 11: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 2 Jul 2025 10:37:50 +1000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 RME（Runtime Memory Encryption）功能，特别是允许虚拟机监控器（VMM）设置 RIPAS（Runtime Integrity Protection Access Settings）。原始的 patch 是针对该功能的实现，旨在增强虚拟化环境中的安全性。

在历史讨论中，参与者对 patch 的细节进行了审查，提出了一些小的修改建议，主要集中在代码的可读性和结构上。Gavin Shan 和 Suzuki K Poulose 等人对 patch 的整体方向表示认可，但也指出了一些需要改进的地方，例如 enum 的设计和函数参数的适用性。

在本周的新讨论中，Steven Price 和 Gavin Shan 继续探讨了 patch 的细节，特别是关于 enum 的扩展以支持 RMI_RTT_SET_S2AP 的问题。Gavin 对于 enum 的设计表示理解，并提到自己刚开始研究 RMMv1.1 的实现，对其细节尚不完全掌握。此外，Joey Gouly 也参与了关于其他相关 patch 的讨论，指出了一些代码逻辑上的问题，并与 Steven 进行了有效的交流。

总体来看，本周的讨论集中在对 patch 的细节优化和对 RMMv1.1 规范的理解上，推动了该功能的进一步完善。

#### 📝 邮件列表

1. **[07-02 10:37]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[07-03 14:22]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[07-09 15:42]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
4. **[07-09 15:42]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
5. **[07-09 15:49]** Re: [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[07-09 16:29]** Re: [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
7. **[07-10 15:24]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 12: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 27 Jun 2025 14:49:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下阻止可缓存 PFNMAP（Page Frame Number Mapping）映射的补丁（PATCH v9 3/6）。

**原始补丁内容**：该补丁旨在解决 arm64 中 PFNMAP 映射的可缓存性问题，确保在使用 `remap_pfn_range()` 函数时，不会错误地假设 VM_PFNMAP VMA（虚拟内存区域）是物理连续的。

**之前讨论要点**：在历史讨论中，参与者指出了当前实现中的潜在问题，特别是 Paolo 提到的 `get_vma_page_shift()` 函数的假设可能导致错误。Ankit 提出了可能需要新的 VMA 标志来帮助驱动与 KVM 之间的映射优化，而 Jason 则建议不应尝试扩展连续性，应该依赖主机发现连续性。此外，Will 对于如何确保驱动在使用 `remap_pfn_range()` 时不会导致过时映射的担忧也引发了讨论。

**本周新讨论进展**：在本周的讨论中，Will 认识到他之前误解了 `remap_pfn_range()` 的行为，认为该函数会自动取消现有映射，但实际上并非如此。这一澄清为后续讨论提供了更清晰的基础，参与者们继续探讨如何在不引入新标志的情况下，优化 PFNMAP 的映射处理。整体来看，讨论围绕着如何确保映射的正确性和性能展开。

#### 📝 邮件列表

1. **[06-27 14:49]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
2. **[06-30 01:56]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
3. **[06-30 09:25]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
4. **[07-04 14:21]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: David Hildenbrand <david@redhat.com>
5. **[07-04 17:04]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
6. **[07-04 13:47]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
7. **[07-08 13:47]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 13: [PATCH] KVM: arm64: fix u64_replace_bits() usage

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 11 Jul 2025 09:27:47 +0200

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `u64_replace_bits()` 函数的使用问题。该函数返回一个修改后的值，但并不直接修改其参数，这在代码中引发了警告，提示忽略了一个有返回值的函数的结果。补丁的主要内容是将 `val` 的赋值更新为 `val = u64_replace_bits(val, hpmn, MDCR_EL2_HPMN);`，以确保正确更新 `val` 的值。

在之前的讨论中，Arnd Bergmann 提到该问题已被 Ben 的补丁修复，但其他参与者指出，Ben 的修复并未在当前的 -next 分支中，因此可能会导致问题。Marc Zyngier 进一步确认了这一点，并表示他已经为 6.16 版本排队了一个修复。

本周的新讨论中，参与者们确认了补丁的必要性，并讨论了 Ben 的修复与当前 -next 分支的关系。Marc Zyngier 强调需要将该修复添加到 -next 分支，以确保在待处理的修复测试覆盖中得到验证，从而避免类似问题的发生。总体来看，讨论集中在确保修复的有效性和及时性上。

#### 📝 邮件列表

1. **[07-11 09:27]** [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Arnd Bergmann <arnd@kernel.org>
2. **[07-11 16:02]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
3. **[07-11 09:36]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-11 10:44]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Arnd Bergmann <arnd@arndb.de>
5. **[07-11 09:53]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-11 10:13]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 14: [PATCH v3 05/10] KVM: arm64: Add trap configs for PMSDSFR_EL1

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 9 Jul 2025 10:53:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，具体是关于添加 PMSDSFR_EL1 的陷阱配置。该补丁的目的是确保在虚拟化环境中，来宾操作系统不会错误地访问 PMSDSFR_EL1 寄存器。

在历史讨论中，参与者 James Clark 指出，正常行为的来宾不会尝试访问该寄存器，因为 PMSDSFR_EL1 的存在是通过访问 PMSDSFR_EL1.FDS 进行检查的，而当前该字段设置为 `undef_access`，并且在 `read_sanitised_id_aa64dfr0_el1()` 函数中隐藏了 SPE（可扩展性能监控单元）对来宾的可见性。Joey Gouly 对此进行了审核并表示支持。

在本周的新讨论中，主要集中在另一个补丁（PATCH v3 08/10）上，涉及处理来自主机的 FFA_MEM_LEND 调用。DaeRo Lee 对该补丁提出了问题，询问在将 FFA_MEM_LEND 视为与 FFA_MEM_SHARE 相同的情况下，主机是否仍然可以访问已借出的内存。Will Deacon 回应称，只有在可信任的区域实现存在问题时，才会依赖 NS 超级管理程序进行隔离。此外，DaeRo Lee 进一步探讨了 pKVM 在主机与非安全来宾虚拟机之间的隔离管理，Will Deacon 则澄清了 pKVM 并不使用 FF-A 来管理主机与来宾的页面所有权。

总体来看，本周的讨论主要围绕内存管理和隔离机制展开，参与者们对补丁的实现细节进行了深入探讨。

#### 📝 邮件列表

1. **[07-09 10:53]** Re: [PATCH v3 05/10] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[07-12 22:36]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
3. **[07-13 12:26]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>
4. **[07-13 23:59]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
5. **[07-13 21:01]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 15: [PATCH v2 0/2] Fix and add warning of misuse of type##_replace_bits()

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  9 Jul 2025 10:38:06 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复和增强 `type##_replace_bits()` 函数的警告，主要涉及两个补丁（patch）。

**原始 patch/问题内容**：
Ben Horgan 提出了两个补丁，旨在修复 `u64_replace_bits()` 的使用错误，并在相关函数上添加 `__must_check` 注解，以确保返回值被检查，避免误用。

**之前讨论要点**：
在之前的讨论中，提到 `u64_replace_bits()` 的返回值被忽略，导致其效果无效。Horgan 在补丁中将其替换为 `u64p_replace_bits()`，以便在原地更新值。此外，补丁还扩展了对 `_get_bits()` 和 `_encode_bits()` 函数的检查，以保持一致性。

**本周的新讨论、进展或结论**：
本周的讨论中，Horgan 提交了补丁的更新版本，并获得了参与者的认可。Marc Zyngier 和 Yury Norov 确认已将补丁应用到代码库中。Zyngier 还提到，由于该错误仅存在于 6.16 版本，因此不再向之前的内核版本回溯。整体来看，本周的讨论进展顺利，补丁已成功整合。

#### 📝 邮件列表

1. **[07-09 10:38]** [PATCH v2 0/2] Fix and add warning of misuse of type##_replace_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-09 10:38]** [PATCH v2 1/2] KVM: arm64: Fix enforcement of upper bound on MDCR_EL2.HPMN
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[07-09 10:38]** [PATCH v2 2/2] bitfield: Ensure the return values of helper functions are checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[07-09 13:22]** Re: (subset) [PATCH v2 1/2] KVM: arm64: Fix enforcement of upper bound on MDCR_EL2.HPMN
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-09 11:33]** Re: [PATCH v2 2/2] bitfield: Ensure the return values of helper
 functions are checked
   - 发件人: Yury Norov <yury.norov@gmail.com>

---

### Thread 16: [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 01 Jul 2025 22:06:33 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中支持 FF-A 1.2 及 SEND_DIRECT2 ABI 的一系列补丁（patch）。原始补丁集包含五个部分，主要目的是为了实现 FF-A 1.2 规范中引入的新 SEND_DIRECT2 ABI，该 ABI 允许使用 x4-x17 寄存器作为消息负载。补丁还确保主机不会使用低于与虚拟机监控器（hypervisor）协商的 FF-A 版本。

在历史讨论中，Per Larsen 提出了补丁的背景和必要性，Marc Zyngier 对补丁中的某些寄存器使用提出了质疑，认为不应随意更改这些寄存器的值。

本周的新讨论中，Per Larsen 针对 Marc Zyngier 的质疑进行了回应，引用了 DEN0077A 1.2 规范中关于保留参数寄存器的规定，强调只要将保留寄存器写入零，就符合规范要求。此外，他还详细分析了 FF-A 1.2 规范中关于状态机的内容，指出在特定情况下，32 位的 FFA_MSG_WAIT 调用可以返回 64 位的 FFA_MSG_SEND_DIRECT_REQ2 响应，进一步支持了补丁的合理性。

总体而言，本周的讨论推动了对补丁的理解，并为其在实现 FF-A 1.2 支持方面提供了理论依据。

#### 📝 邮件列表

1. **[07-01 22:06]** [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-01 22:06]** [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-03 13:38]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization and in host handler
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-07 17:06]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>

---

### Thread 17: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 4 Jul 2025 18:18:24 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM 架构性能监控单元（PMU）分支记录缓冲区扩展（BRBE）的补丁。该补丁的主要内容是为 ARM PMUv3 增加对 BRBE 的支持，旨在提升性能监控的能力。

在历史讨论中，参与者 Mark Rutland 对补丁表示认可，并提出了一些需要修正的细节。他提到在之前的版本中，函数 `brbe_invalidate()` 的位置调整至 `brbe_read_filtered_entries()` 中，以便在事件溢出时读取条目。Rutland 认为补丁整体上已经具备应用的条件，并询问 Will 是否愿意在合并时处理相关的差异。

在本周的新讨论中，Rob Herring 和 Mark Rutland 继续探讨了 PMU 中断带来的样本不连续性问题。Herring 表示，这种不连续性可能不会对实际应用产生重大影响，因为需要在短时间内发生两次 PMU 中断才能丢失样本。Will Deacon 随后确认已将补丁应用到其分支中，并列出了补丁的四个部分，包括 BRBE 寄存器的添加、启动要求的处理，以及在 nVHE 虚拟机中禁用分支生成的相关补丁。

总体而言，讨论进展顺利，补丁已被接受并应用，相关问题也得到了充分的讨论与解决。

#### 📝 邮件列表

1. **[07-04 18:18]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[07-07 10:57]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
3. **[07-08 19:02]** Re: [PATCH v23 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 18: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Jun 2025 17:12:20 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）的补丁系列，主题为“提供一个能力以禁用 APERF/MPERF 读取拦截”。该补丁的主要目的是允许虚拟机监控器（VMM）控制来宾对 IA32_APERF 和 IA32_MPERF 的读取权限，从而帮助来宾确定物理逻辑处理单元（LPU）的有效频率倍增器。

在历史讨论中，Sean Christopherson 提到该补丁系列的最后一部分是为了处理 ARM64 相关的自测试更改，并且可以在不影响 x86 部分的情况下被忽略。补丁的背景是之前的提交（如 b51700632e0e）允许用户空间 VMM 授予来宾读取某些 MSR（模型特定寄存器）的权限。

在本周的新讨论中，Sean Christopherson 更新了补丁的状态，表示已将其应用于 kvm-x86 的杂项分支，并修复了一个拼写错误。他还提供了补丁系列中每个补丁的链接，展示了补丁的具体内容和自测试的扩展。

总结而言，本周的进展是补丁已成功应用，且相关的自测试也得到了扩展，标志着该功能的进一步完善。

#### 📝 邮件列表

1. **[06-25 17:12]** [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-10 16:08]** Re: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF
 read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 19: [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 27 Jun 2025 10:09:01 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 GICv5 主机上启用 GICv3 客户机的补丁系列，主要通过利用 GICv5 的遗留兼容性特性（FEAT_GCIE_LEGACY）来实现。该补丁的主要目标是使现有的 GICv3 虚拟机能够在 GICv5 系统上运行，而无需对虚拟机或虚拟机监控器进行修改。

在历史讨论中，Sascha Bischoff 提出了这一补丁系列，强调了两个主要的改动方向：一是 KVM GIC 支持，确保能够检测到 GICv5 主机并配置其以支持 GICv3 客户机；二是 IRQ 芯片支持，确保转发的 PPI 中断能够正常工作。

在本周的新讨论中，Oliver Upton 更新了补丁的进展，表示他已经将这些补丁应用到 -next 分支中，并对 KVM 部分的实现表示满意。不过，他也提到这些补丁是否能在 6.17 版本中落地还不确定，取决于主机端的实现情况。补丁的具体内容包括对 GICv5 的中断处理、结构体填充以及对 GICv3 兼容性的支持等。

#### 📝 邮件列表

1. **[06-27 10:09]** [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[07-08 15:24]** Re: [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using FEAT_GCIE_LEGACY
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 9 Jul 2025 18:57:00 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 PowerPC 架构的补丁，标题为“[PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches”。该补丁旨在解决 KCOV 在 __init 和内联函数之间的不匹配问题。

在历史讨论中，并没有提供具体的背景信息或之前的讨论内容，因此我们无法得知此补丁的详细背景或先前的争议。

在本周的新讨论中，参与者 Kees Cook 对补丁表示认可，并表示将采纳该补丁，同时放弃自己之前的补丁。这表明该补丁得到了积极的反馈，并可能在后续的版本中被合并。

总结来看，这个补丁的主要目的是解决 PowerPC 架构中 KCOV 的初始化与内联函数之间的兼容性问题，当前讨论显示出对该补丁的支持，预示着其可能会在未来的更新中被采纳。

#### 📝 邮件列表

1. **[07-09 18:57]** Re: [PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 21: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 9 Jul 2025 16:12:18 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的定时器处理，特别是允许在没有 CNTPOFF_EL2 的情况下使用物理偏移的补丁（PATCH v4 05/20）。

在历史讨论中，补丁的主要目的是改善 KVM 对物理定时器的支持，尤其是在处理定时器中断时的准确性和效率。补丁的背景是针对当前实现中存在的定时器延迟问题，尤其是在特定硬件平台（如 Kunpeng920）上测试时，发现定时器的返回时间过长。

本周的讨论中，参与者 Zenghui Yu 分享了在测试 `arch_timer_edge_cases` 时的观察结果。他指出，在测试物理定时器时，`test_timer_cval()` 函数的注释存在误导，实际行为与预期不符，导致没有触发物理定时器中断。Zenghui 详细描述了定时器状态的设置过程，并指出该测试用例并不代表实际使用场景，质疑是否应该或能够正确模拟这种情况。

总结而言，本周的讨论揭示了补丁在实际应用中的一些潜在问题，并引发了对定时器行为的进一步思考。

#### 📝 邮件列表

1. **[07-09 16:12]** Re: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH] tools: Remove obsolete 32-bit arm kvm.h header file

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 10 Jul 2025 12:25:19 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于移除过时的32位ARM KVM头文件（kvm.h）。该补丁由Thomas Huth提出，目的是在之前的提交（541ad0150ca4a）中已经移除了32位ARM KVM主机支持后，进一步清理工具目录中的冗余文件。

在历史讨论中，补丁的背景是由于32位ARM KVM主机支持的移除，相关的头文件也不再需要，因此提出了删除该文件的建议。邮件中提到，此次补丁被标记为RFC（请求反馈），因为作者目前没有32位ARM的构建环境，尚未进行编译测试。

在本周的新讨论中，Thomas Huth再次确认了该补丁的必要性，并提供了具体的删除操作，包括删除了315行的kvm.h文件及相关的检查脚本更新。邮件中没有其他参与者的反馈或讨论，因此目前尚未有进一步的进展或结论。

#### 📝 邮件列表

1. **[07-10 12:25]** [RFC PATCH] tools: Remove obsolete 32-bit arm kvm.h header file
   - 发件人: Thomas Huth <thuth@redhat.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] WARNING in pend_serror_exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 17:06:30 -0700

#### 🤖 AI 总结

本邮件主题为“[syzbot] [kvmarm?] WARNING in pend_serror_exception”，是由 syzbot 生成的报告，指出在 Linux 内核的 KVM ARM 相关代码中出现了一个警告，具体位置在 `pend_serror_exception` 函数。报告中提供了相关的内核版本、编译器信息、用户空间架构及重现步骤等详细信息。

在历史讨论部分没有相关内容，因此本周的新讨论是唯一的信息来源。此次报告中，syzbot 发现的问题与 ARM64 架构的 KVM 虚拟化相关，涉及到错误注入的处理。报告中详细列出了调用栈和相关的 CPU 状态信息，指出了可能导致问题的代码位置，帮助开发者定位和修复该问题。

目前尚未有针对该问题的修复进展或讨论，syzbot 提供了后续跟踪和反馈的方式，鼓励开发者在解决问题后添加相应的标签，以便于问题的管理和记录。

#### 📝 邮件列表

1. **[07-12 17:06]** [syzbot] [kvmarm?] WARNING in pend_serror_exception
   - 发件人: syzbot <syzbot+1f6f096afda6f4f8f565@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 3 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #4

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 16:20:23 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，旨在为 6.16 版本提供改进。历史讨论中，Marc Zyngier 提到此次补丁主要包括三个方面的修复：允许 pKVM 初始化失败而不影响主机运行、确保主机 S2 不会映射过多内容，以及对嵌套 GICv3 模拟的一个小错误修复。

在本周的新讨论中，Paolo Bonzini 确认了补丁的合并，并提到在此过程中 git:// 协议出现了问题，建议使用 https:// 进行访问。Marc Zyngier 对此表示疑惑，询问是否有相关公告，并确认自己仍然可以使用 git:// 协议进行克隆。随后，Paolo 也表示问题已经解决，推测可能是 git.kernel.org 的临时故障。

总体来看，本周的讨论主要集中在补丁的合并确认及访问协议的问题上，未涉及新的技术讨论或补丁内容。

#### 📝 邮件列表

1. **[06-26 16:20]** [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-08 16:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[07-08 19:06]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-10 12:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 2: [GIT PULL] KVM/arm64 fixes for 6.16, take #5

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  3 Jul 2025 11:05:44 +0100

#### 🤖 AI 总结

在本次邮件讨论中，Marc Zyngier 提出了一个关于 KVM/arm64 的修复补丁，旨在解决 6.16 版本中的一些问题。该补丁主要包括删除过去修复中遗留的内容，如去除主机 FPSIMD 状态的 EL1 S1 映射，并停止向客户机报告虚假的 S2 基础粒度大小。

在历史讨论中，Marc 提到这一系列修复的严重性逐渐降低，并期望将此补丁与上周的 kvmarm-fixes-6.16-4 合并提交。

在本周的新讨论中，Paolo Bonzini 确认补丁将在 KVM 社区会议后提交给 Linus，表明该补丁的进展顺利，预计将很快被合并。这表明社区对该补丁的支持和认可，进一步推动了 KVM/arm64 的稳定性改进。

#### 📝 邮件列表

1. **[07-03 11:05]** [GIT PULL] KVM/arm64 fixes for 6.16, take #5
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-08 16:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #5
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 3: [GIT PULL] KVM/arm64 fixes for 6.16, take #6

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 11 Jul 2025 09:48:34 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 6.16 版本中的修复，Marc Zyngier 提出了一个补丁，旨在解决在嵌套虚拟化中处理 PMU 寄存器数量的清理问题。

在历史讨论中，没有提供具体的背景信息或之前的补丁内容，因此我们无法了解该补丁的前因后果。

本周的新讨论中，Marc Zyngier 提交了一个修复补丁，主要针对 MDCR_EL2.HPMN 的上限强制执行问题。补丁修复了在调整客体视图时使用 `u64_replace_bits()` 函数的错误。邮件中提到，此补丁是针对 6.16 版本的最后一次修复，确保了在嵌套虚拟化环境中对 PMU 寄存器的正确处理。

总结来说，本周的进展主要集中在修复 KVM/arm64 的一个特定问题，并且该补丁已准备好供合并。

#### 📝 邮件列表

1. **[07-11 09:48]** [GIT PULL] KVM/arm64 fixes for 6.16, take #6
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 4 个 thread

---

### Thread 1: [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  4 Jul 2025 17:12:55 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 RISC-V 架构的 KVM 工具支持的补丁。历史讨论中，Andrew Jones 提出了两个补丁：第一个补丁确保在非 ARM 主机上运行 KVM 工具时的架构正确性，第二个补丁则是为 RISC-V 添加 KVM 工具支持，使其能够作为一类公民运行测试。

在之前的讨论中，Andrew 指出 KVM 工具在非 ARM 主机上无法正常工作，并强调 RISC-V 需要特定的修改以支持 KVM 工具。他的补丁涉及多个文件的修改，包括 README.md 和配置文件。

在本周的新讨论中，Jesse Taube 和 Nutty Liu 对两个补丁进行了审核并表示支持，确认了补丁的有效性。Jesse 还提出了是否计划为 i386 和 x86_64 添加支持的疑问，并建议在 ARM 上添加额外的检查。Andrew 进一步回应，表示目前没有计划，但认为这是一个好的建议，并提到 ARM KVM 已被弃用，建议移除与 HOST==arm 相关的引用。最终，Andrew 确认已将补丁合并，标志着这一讨论的阶段性结束。

#### 📝 邮件列表

1. **[07-04 17:12]** [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[07-04 17:12]** [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch with kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[07-04 17:12]** [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
4. **[07-07 08:10]** Re: [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch
 with kvmtool
   - 发件人: Jesse Taube <jesse@rivosinc.com>
5. **[07-07 08:28]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Jesse Taube <jesse@rivosinc.com>
6. **[07-07 19:44]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
7. **[07-08 11:41]** Re: [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch with kvmtool
   - 发件人: Nutty Liu <liujingqi@lanxincomputing.com>
8. **[07-08 11:43]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Nutty Liu <liujingqi@lanxincomputing.com>
9. **[07-08 11:00]** Re: [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 16:48:00 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM 单元测试中添加 kvmtool 的补丁（PATCH v4 00/13）。该补丁的目标是简化测试运行过程，使用户能够通过简单的命令配置和运行所有测试。kvmtool 相较于 qemu 更小且易于修改，适合开发者在 KVM 中添加或原型化新特性。

在历史讨论中，Alexandru Elisei 提到 kvmtool 的默认行为会自动创建根文件系统并添加额外的内核参数，这可能会对某些测试造成干扰，因为这些测试会解析内核命令行并可能因遇到额外选项而失败。为了解决这个问题，kvmtool 引入了 `--nodefaults` 命令行参数。

在本周的新讨论中，Thomas Huth 提出了在 s390x 上出现的一个问题，提示 `vmm_defaults_opts` 命令未找到。Andrew Jones 随后回应，指出该问题已通过他最近提交的补丁修复。Thomas 对此表示感谢，并为之前未注意到该补丁而道歉。

总结来看，本周的讨论主要集中在解决 kvmtool 集成中的具体问题，并确认了相关补丁的有效性。

#### 📝 邮件列表

1. **[06-25 16:48]** [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:48]** [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[07-11 13:32]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Thomas Huth <thuth@redhat.com>
4. **[07-11 16:35]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
5. **[07-11 16:37]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Thomas Huth <thuth@redhat.com>

---

### Thread 3: [syzbot] [kvmarm?] WARNING in pend_sync_exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 18:45:31 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM ARM 虚拟化中的一个警告问题，具体是出现在 `pend_sync_exception` 函数中的错误。此问题由 syzbot 自动检测到，相关的内核提交为 `15724a984643`，该提交合并了 `kvm-arm64/doublefault2` 分支。

在历史讨论中，没有提供具体的背景信息或之前的讨论内容，因此我们无法得知该问题是否有先前的讨论或补丁。

在本周的新讨论中，syzbot 提供了详细的错误报告，包括发生错误的上下文、相关的硬件信息、内核版本以及重现该问题的用户空间代码和 C 代码示例。报告中指出，错误发生在 `pend_sync_exception` 函数的第 63 行，并附带了调用栈信息，帮助开发者定位问题。syzbot 还请求如果有人修复了该问题，请在提交中添加特定的标签以便追踪。

总体来看，目前该问题尚未得到解决，开发者被鼓励对其进行调查和修复。

#### 📝 邮件列表

1. **[07-12 18:45]** [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>

---

### Thread 4: [QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 22:55:13 +0900

#### 🤖 AI 总结

本邮件讨论主题为“[QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host”，主要涉及对 KVM 在 arm64 架构下处理 FFA_MEM_LEND 调用的相关问题。

在本周的新讨论中，参与者 daeroro 向 Will 提出了一个具体问题，询问将 FFA_MEM_LEND 视为与 FFA_MEM_SHARE 相同的处理方式是否意味着主机在内存被“借出”后仍然可以访问该内存。这表明对内存访问权限和管理的关注，尤其是在虚拟化环境中如何安全地处理资源共享。

目前没有提供历史讨论的内容，因此无法总结之前的讨论要点。整体来看，本周的讨论集中在对内存管理机制的理解和潜在影响上，反映出参与者对 KVM 和 arm64 架构下资源共享的深入思考。

#### 📝 邮件列表

1. **[07-12 22:55]** [QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: daeroro <skseofh@gmail.com>

---

